; Auto-generated. Do not edit!


(cl:in-package nav-srv)


;//! \htmlinclude Service_msg-request.msg.html

(cl:defclass <Service_msg-request> (roslisp-msg-protocol:ros-message)
  ((direction
    :reader direction
    :initarg :direction
    :type cl:fixnum
    :initform 0)
   (velocity
    :reader velocity
    :initarg :velocity
    :type cl:fixnum
    :initform 0)
   (rotation
    :reader rotation
    :initarg :rotation
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Service_msg-request (<Service_msg-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Service_msg-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Service_msg-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nav-srv:<Service_msg-request> is deprecated: use nav-srv:Service_msg-request instead.")))

(cl:ensure-generic-function 'direction-val :lambda-list '(m))
(cl:defmethod direction-val ((m <Service_msg-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nav-srv:direction-val is deprecated.  Use nav-srv:direction instead.")
  (direction m))

(cl:ensure-generic-function 'velocity-val :lambda-list '(m))
(cl:defmethod velocity-val ((m <Service_msg-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nav-srv:velocity-val is deprecated.  Use nav-srv:velocity instead.")
  (velocity m))

(cl:ensure-generic-function 'rotation-val :lambda-list '(m))
(cl:defmethod rotation-val ((m <Service_msg-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nav-srv:rotation-val is deprecated.  Use nav-srv:rotation instead.")
  (rotation m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Service_msg-request>) ostream)
  "Serializes a message object of type '<Service_msg-request>"
  (cl:let* ((signed (cl:slot-value msg 'direction)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'velocity)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'rotation)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Service_msg-request>) istream)
  "Deserializes a message object of type '<Service_msg-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'direction) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'velocity) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'rotation) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Service_msg-request>)))
  "Returns string type for a service object of type '<Service_msg-request>"
  "nav/Service_msgRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service_msg-request)))
  "Returns string type for a service object of type 'Service_msg-request"
  "nav/Service_msgRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Service_msg-request>)))
  "Returns md5sum for a message object of type '<Service_msg-request>"
  "86301fa8233c7fe1657e8060a290c050")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Service_msg-request)))
  "Returns md5sum for a message object of type 'Service_msg-request"
  "86301fa8233c7fe1657e8060a290c050")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Service_msg-request>)))
  "Returns full string definition for message of type '<Service_msg-request>"
  (cl:format cl:nil "int16 direction~%int16 velocity~%int16 rotation~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Service_msg-request)))
  "Returns full string definition for message of type 'Service_msg-request"
  (cl:format cl:nil "int16 direction~%int16 velocity~%int16 rotation~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Service_msg-request>))
  (cl:+ 0
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Service_msg-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Service_msg-request
    (cl:cons ':direction (direction msg))
    (cl:cons ':velocity (velocity msg))
    (cl:cons ':rotation (rotation msg))
))
;//! \htmlinclude Service_msg-response.msg.html

(cl:defclass <Service_msg-response> (roslisp-msg-protocol:ros-message)
  ((receive_data
    :reader receive_data
    :initarg :receive_data
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Service_msg-response (<Service_msg-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Service_msg-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Service_msg-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nav-srv:<Service_msg-response> is deprecated: use nav-srv:Service_msg-response instead.")))

(cl:ensure-generic-function 'receive_data-val :lambda-list '(m))
(cl:defmethod receive_data-val ((m <Service_msg-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nav-srv:receive_data-val is deprecated.  Use nav-srv:receive_data instead.")
  (receive_data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Service_msg-response>) ostream)
  "Serializes a message object of type '<Service_msg-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'receive_data) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Service_msg-response>) istream)
  "Deserializes a message object of type '<Service_msg-response>"
    (cl:setf (cl:slot-value msg 'receive_data) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Service_msg-response>)))
  "Returns string type for a service object of type '<Service_msg-response>"
  "nav/Service_msgResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service_msg-response)))
  "Returns string type for a service object of type 'Service_msg-response"
  "nav/Service_msgResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Service_msg-response>)))
  "Returns md5sum for a message object of type '<Service_msg-response>"
  "86301fa8233c7fe1657e8060a290c050")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Service_msg-response)))
  "Returns md5sum for a message object of type 'Service_msg-response"
  "86301fa8233c7fe1657e8060a290c050")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Service_msg-response>)))
  "Returns full string definition for message of type '<Service_msg-response>"
  (cl:format cl:nil "bool receive_data~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Service_msg-response)))
  "Returns full string definition for message of type 'Service_msg-response"
  (cl:format cl:nil "bool receive_data~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Service_msg-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Service_msg-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Service_msg-response
    (cl:cons ':receive_data (receive_data msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Service_msg)))
  'Service_msg-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Service_msg)))
  'Service_msg-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service_msg)))
  "Returns string type for a service object of type '<Service_msg>"
  "nav/Service_msg")