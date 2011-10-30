#!/usr/bin/python
#
# Provides Mapper, a class which uses state estimates and LIDAR scan
# data to fill an occupancy grid.

import roslib; roslib.load_manifest('farley_ros')
import rospy
from sensor_msgs.msg import LaserScan
from farley_ros.msg import StateEstimate

import numpy as np
import math as m
from collections import namedtuple


MapPose = namedtuple('MapPose', 'x y h')
Range = namedtuple('Range', 'min max incr')

class Mapper:
  def __init__(self):
    rospy.Subscriber('/scan', LaserScan, self._scanCb)
    rospy.Subscriber('state_est', StateEstimate, self._stateCb)

    self.alpha = 0.05

    #Logit Probabilities
    self.highP = m.log10(0.7/(1-0.7))
    self.lowP  = m.log10(0.3/(1-0.3))

    self.scanAngle = None
    self.scanRange = None

    # Map extents and resolution [m]
    self.x = Range(-1, 1, 0.25)
    self.y = Range(-1, 1, 0.25)

    # Current robot pose:
    self.pose = None

    # The actual occupancy grid
    self.grid = np.zeros((
        (self.x.max - self.x.min)/self.x.incr + 1,
        (self.y.max - self.y.min)/self.y.incr + 1 )) 
    # Map grid index -> (x,y)
    self.xAxis = np.linspace(self.x.min, self.x.max, self.grid.shape[0])
    self.yAxis = np.linspace(self.y.min, self.y.max, self.grid.shape[1])

  def getCell(self, x, y):
    """ Get the grid cell value at coordinates (x,y) [m] 
        Return None if out of range. """
    if (x > self.x.max) or (x < self.x.min) or (y > self.y.max) or (y < self.y.min):
      return None
    return self.grid[(x - self.x.min)/self.x.incr, (y - self.y.min)/self.x.incr]

  def setCell(self, x, y, val):
    """ Set the value of the grid cell at coordinate (x,y) to [val] 
        Does nothing if x, y out of range. """
    if (x > self.x.max) or (x < self.x.min) or (y > self.y.max) or (y < self.y.min):
      return 
    self.grid[(x - self.x.min)/self.x.incr, (y - self.y.min)/self.y.incr] = val

  def getScanInx(self, scan, angle):
    """ Determine which scan range measurement is closest to the given
        angle (relative to robot heading) """
    if (angle < self.scanAngle.min) or (angle > self.scanAngle.max):
      return None
  
    # Calculate the index of the closest scan direction:
    return int((angle - self.scanAngle.min) / self.scanAngle.incr)


  def getRange(self, scan, angle):
    """ Gets the range measurement for a particular direction relative to
        the robot heading, from a LIDAR scan message.
        Returns None if direction is out of scanner range. """
    # Calculate the index of the closest scan direction:
    inx = self.getScanInx(scan, angle)
    if inx is None:
      return None
    return scan.ranges[inx]

  def getCellAngle(self, xInx, yInx):
    """ Returns the angle of the specified grid cell relative to the current
        pose. """
    absAng = m.atan2(self.yAxis[yInx] - self.pose.y, 
                     self.xAxis[xInx] - self.pose.x)
    rel = absAng - self.pose.h
    # Wrap rel to [-pi, pi]
    while rel < -m.pi:
      rel += 2*m.pi
    while rel > m.pi:
      rel -= 2*m.pi

    return rel

  def getDistance(self, xInx, yInx):
    """ Calculates the distance from a specified grid cell to the current 
        pose. """
    xDist = self.xAxis[xInx] - self.pose.x
    yDist = self.yAxis[yInx] - self.pose.y
    return m.sqrt(xDist*xDist + yDist*yDist)

  def _updateCell(self, xi, yi, scan):
    """ Updates a specific cell with new LIDAR data """
    # Angle to this cell:
    ang = self.getCellAngle(xi, yi)
    # Distance to this cell:
    cellDist = self.getDistance(xi, yi)
    # Nearest obstacle in the direction of the cell:
    nearest = self.getRange(scan, ang)
    
    if (nearest is None) or (nearest > self.scanRange.max) \
        or (nearest < self.scanRange.min) or (cellDist > nearest+self.alpha):
      # Out of scanner range or behind an obstacle, do not change the existing range information
      pass
    elif (abs(nearest - cellDist) < self.alpha):
      self.grid[xi,yi] += self.highP
    else:
      self.grid[xi,yi] += self.lowP
    return

  def _scanCb(self, scan):
    if self.scanAngle is None:
      print('Angle - min: {0} +: {1} max: {2}'.format(
          scan.angle_min, scan.angle_increment, scan.angle_max))
      print('Range - min: {0} max: {1}'.format(scan.range_min, scan.range_max))

    self.scanAngle = Range(scan.angle_min, scan.angle_max, scan.angle_increment)
    self.scanRange = Range(scan.range_min, scan.range_max, None)

    if self.pose is None:
      # Need state estimate to do mapping
      return

    # Update each map cell:
    for xi in range(self.grid.shape[0]):
      for yi in range(self.grid.shape[1]):
        self._updateCell(xi, yi, scan)

    print(self.grid)

  def _stateCb(self, state):
    # state.state is [vel, heading, x pos, y pos]
    self.pose = MapPose(state.state[2], state.state[3], state.state[1])
#    print(self.pose)

