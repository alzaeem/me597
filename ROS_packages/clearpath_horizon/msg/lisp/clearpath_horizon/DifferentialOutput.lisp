; Auto-generated. Do not edit!


(in-package clearpath_horizon-msg)


;//! \htmlinclude DifferentialOutput.msg.html

(defclass <DifferentialOutput> (ros-message)
  ((header
    :reader header-val
    :initarg :header
    :type roslib-msg:<Header>
    :initform (make-instance 'roslib-msg:<Header>))
   (left
    :reader left-val
    :initarg :left
    :type float
    :initform 0.0)
   (right
    :reader right-val
    :initarg :right
    :type float
    :initform 0.0))
)
(defmethod serialize ((msg <DifferentialOutput>) ostream)
  "Serializes a message object of type '<DifferentialOutput>"
  (serialize (slot-value msg 'header) ostream)
  (let ((bits (roslisp-utils:encode-double-float-bits (slot-value msg 'left))))
    (write-byte (ldb (byte 8 0) bits) ostream)
    (write-byte (ldb (byte 8 8) bits) ostream)
    (write-byte (ldb (byte 8 16) bits) ostream)
    (write-byte (ldb (byte 8 24) bits) ostream)
    (write-byte (ldb (byte 8 32) bits) ostream)
    (write-byte (ldb (byte 8 40) bits) ostream)
    (write-byte (ldb (byte 8 48) bits) ostream)
    (write-byte (ldb (byte 8 56) bits) ostream))
  (let ((bits (roslisp-utils:encode-double-float-bits (slot-value msg 'right))))
    (write-byte (ldb (byte 8 0) bits) ostream)
    (write-byte (ldb (byte 8 8) bits) ostream)
    (write-byte (ldb (byte 8 16) bits) ostream)
    (write-byte (ldb (byte 8 24) bits) ostream)
    (write-byte (ldb (byte 8 32) bits) ostream)
    (write-byte (ldb (byte 8 40) bits) ostream)
    (write-byte (ldb (byte 8 48) bits) ostream)
    (write-byte (ldb (byte 8 56) bits) ostream))
)
(defmethod deserialize ((msg <DifferentialOutput>) istream)
  "Deserializes a message object of type '<DifferentialOutput>"
  (deserialize (slot-value msg 'header) istream)
  (let ((bits 0))
    (setf (ldb (byte 8 0) bits) (read-byte istream))
    (setf (ldb (byte 8 8) bits) (read-byte istream))
    (setf (ldb (byte 8 16) bits) (read-byte istream))
    (setf (ldb (byte 8 24) bits) (read-byte istream))
    (setf (ldb (byte 8 32) bits) (read-byte istream))
    (setf (ldb (byte 8 40) bits) (read-byte istream))
    (setf (ldb (byte 8 48) bits) (read-byte istream))
    (setf (ldb (byte 8 56) bits) (read-byte istream))
    (setf (slot-value msg 'left) (roslisp-utils:decode-double-float-bits bits)))
  (let ((bits 0))
    (setf (ldb (byte 8 0) bits) (read-byte istream))
    (setf (ldb (byte 8 8) bits) (read-byte istream))
    (setf (ldb (byte 8 16) bits) (read-byte istream))
    (setf (ldb (byte 8 24) bits) (read-byte istream))
    (setf (ldb (byte 8 32) bits) (read-byte istream))
    (setf (ldb (byte 8 40) bits) (read-byte istream))
    (setf (ldb (byte 8 48) bits) (read-byte istream))
    (setf (ldb (byte 8 56) bits) (read-byte istream))
    (setf (slot-value msg 'right) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(defmethod ros-datatype ((msg (eql '<DifferentialOutput>)))
  "Returns string type for a message object of type '<DifferentialOutput>"
  "clearpath_horizon/DifferentialOutput")
(defmethod md5sum ((type (eql '<DifferentialOutput>)))
  "Returns md5sum for a message object of type '<DifferentialOutput>"
  "8f32685125452f5bdf68130369af5296")
(defmethod message-definition ((type (eql '<DifferentialOutput>)))
  "Returns full string definition for message of type '<DifferentialOutput>"
  (format nil "Header header~%float64 left~%float64 right~%~%================================================================================~%MSG: roslib/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(defmethod serialization-length ((msg <DifferentialOutput>))
  (+ 0
     (serialization-length (slot-value msg 'header))
     8
     8
))
(defmethod ros-message-to-list ((msg <DifferentialOutput>))
  "Converts a ROS message object to a list"
  (list '<DifferentialOutput>
    (cons ':header (header-val msg))
    (cons ':left (left-val msg))
    (cons ':right (right-val msg))
))
