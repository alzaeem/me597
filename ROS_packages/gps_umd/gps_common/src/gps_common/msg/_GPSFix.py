"""autogenerated by genmsg_py from GPSFix.msg. Do not edit."""
import roslib.message
import struct

import std_msgs.msg

class GPSFix(roslib.message.Message):
  _md5sum = "0ae01adfd96ac75f78c023bbead08337"
  _type = "gps_common/GPSFix"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header

# Latitude (degrees). Positive is north of equator; negative is south.
float64 latitude

# Longitude (degrees). Positive is east of prime meridian, negative south.
float64 longitude

# Altitude (meters). Positive is above reference (e.g., sea level).
float64 altitude

# Direction (degrees from north)
float64 track

# Ground speed (meters/second)
float64 speed

# Vertical speed (meters/second)
float64 climb

# Device orientation (units in degrees)
float64 pitch
float64 roll
float64 dip

# GPS time
float64 time

# Total (positional-temporal) dilution of precision
float64 gdop

# Positional (3D) dilution of precision
float64 pdop

# Horizontal dilution of precision
float64 hdop

# Vertical dilution of precision
float64 vdop

# Temporal dilution of precision
float64 tdop

# Spherical position uncertainty (meters) [epe]
float64 err

# Horizontal position uncertainty (meters) [eph]
float64 err_horz

# Vertical position uncertainty (meters) [epv]
float64 err_vert

# Track uncertainty (degrees) [epd]
float64 err_track

# Ground speed uncertainty (meters/second) [eps]
float64 err_speed

# Vertical speed uncertainty (meters/second) [epc]
float64 err_climb

# Temporal uncertainty [ept]
float64 err_time

# Orientation uncertainty (degrees)
float64 err_pitch
float64 err_roll
float64 err_dip


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['header','latitude','longitude','altitude','track','speed','climb','pitch','roll','dip','time','gdop','pdop','hdop','vdop','tdop','err','err_horz','err_vert','err_track','err_speed','err_climb','err_time','err_pitch','err_roll','err_dip']
  _slot_types = ['Header','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       header,latitude,longitude,altitude,track,speed,climb,pitch,roll,dip,time,gdop,pdop,hdop,vdop,tdop,err,err_horz,err_vert,err_track,err_speed,err_climb,err_time,err_pitch,err_roll,err_dip
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(GPSFix, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg._Header.Header()
      if self.latitude is None:
        self.latitude = 0.
      if self.longitude is None:
        self.longitude = 0.
      if self.altitude is None:
        self.altitude = 0.
      if self.track is None:
        self.track = 0.
      if self.speed is None:
        self.speed = 0.
      if self.climb is None:
        self.climb = 0.
      if self.pitch is None:
        self.pitch = 0.
      if self.roll is None:
        self.roll = 0.
      if self.dip is None:
        self.dip = 0.
      if self.time is None:
        self.time = 0.
      if self.gdop is None:
        self.gdop = 0.
      if self.pdop is None:
        self.pdop = 0.
      if self.hdop is None:
        self.hdop = 0.
      if self.vdop is None:
        self.vdop = 0.
      if self.tdop is None:
        self.tdop = 0.
      if self.err is None:
        self.err = 0.
      if self.err_horz is None:
        self.err_horz = 0.
      if self.err_vert is None:
        self.err_vert = 0.
      if self.err_track is None:
        self.err_track = 0.
      if self.err_speed is None:
        self.err_speed = 0.
      if self.err_climb is None:
        self.err_climb = 0.
      if self.err_time is None:
        self.err_time = 0.
      if self.err_pitch is None:
        self.err_pitch = 0.
      if self.err_roll is None:
        self.err_roll = 0.
      if self.err_dip is None:
        self.err_dip = 0.
    else:
      self.header = std_msgs.msg._Header.Header()
      self.latitude = 0.
      self.longitude = 0.
      self.altitude = 0.
      self.track = 0.
      self.speed = 0.
      self.climb = 0.
      self.pitch = 0.
      self.roll = 0.
      self.dip = 0.
      self.time = 0.
      self.gdop = 0.
      self.pdop = 0.
      self.hdop = 0.
      self.vdop = 0.
      self.tdop = 0.
      self.err = 0.
      self.err_horz = 0.
      self.err_vert = 0.
      self.err_track = 0.
      self.err_speed = 0.
      self.err_climb = 0.
      self.err_time = 0.
      self.err_pitch = 0.
      self.err_roll = 0.
      self.err_dip = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_25d.pack(_x.latitude, _x.longitude, _x.altitude, _x.track, _x.speed, _x.climb, _x.pitch, _x.roll, _x.dip, _x.time, _x.gdop, _x.pdop, _x.hdop, _x.vdop, _x.tdop, _x.err, _x.err_horz, _x.err_vert, _x.err_track, _x.err_speed, _x.err_climb, _x.err_time, _x.err_pitch, _x.err_roll, _x.err_dip))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg._Header.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 200
      (_x.latitude, _x.longitude, _x.altitude, _x.track, _x.speed, _x.climb, _x.pitch, _x.roll, _x.dip, _x.time, _x.gdop, _x.pdop, _x.hdop, _x.vdop, _x.tdop, _x.err, _x.err_horz, _x.err_vert, _x.err_track, _x.err_speed, _x.err_climb, _x.err_time, _x.err_pitch, _x.err_roll, _x.err_dip,) = _struct_25d.unpack(str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_25d.pack(_x.latitude, _x.longitude, _x.altitude, _x.track, _x.speed, _x.climb, _x.pitch, _x.roll, _x.dip, _x.time, _x.gdop, _x.pdop, _x.hdop, _x.vdop, _x.tdop, _x.err, _x.err_horz, _x.err_vert, _x.err_track, _x.err_speed, _x.err_climb, _x.err_time, _x.err_pitch, _x.err_roll, _x.err_dip))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg._Header.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 200
      (_x.latitude, _x.longitude, _x.altitude, _x.track, _x.speed, _x.climb, _x.pitch, _x.roll, _x.dip, _x.time, _x.gdop, _x.pdop, _x.hdop, _x.vdop, _x.tdop, _x.err, _x.err_horz, _x.err_vert, _x.err_track, _x.err_speed, _x.err_climb, _x.err_time, _x.err_pitch, _x.err_roll, _x.err_dip,) = _struct_25d.unpack(str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_3I = struct.Struct("<3I")
_struct_25d = struct.Struct("<25d")
