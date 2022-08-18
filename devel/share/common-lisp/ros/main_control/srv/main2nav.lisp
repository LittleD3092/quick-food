; Auto-generated. Do not edit!


(cl:in-package main_control-srv)


;//! \htmlinclude main2nav-request.msg.html

(cl:defclass <main2nav-request> (roslisp-msg-protocol:ros-message)
  ((main_x
    :reader main_x
    :initarg :main_x
    :type cl:fixnum
    :initform 0)
   (main_y
    :reader main_y
    :initarg :main_y
    :type cl:fixnum
    :initform 0)
   (rotation
    :reader rotation
    :initarg :rotation
    :type cl:fixnum
    :initform 0))
)

(cl:defclass main2nav-request (<main2nav-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <main2nav-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'main2nav-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name main_control-srv:<main2nav-request> is deprecated: use main_control-srv:main2nav-request instead.")))

(cl:ensure-generic-function 'main_x-val :lambda-list '(m))
(cl:defmethod main_x-val ((m <main2nav-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader main_control-srv:main_x-val is deprecated.  Use main_control-srv:main_x instead.")
  (main_x m))

(cl:ensure-generic-function 'main_y-val :lambda-list '(m))
(cl:defmethod main_y-val ((m <main2nav-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader main_control-srv:main_y-val is deprecated.  Use main_control-srv:main_y instead.")
  (main_y m))

(cl:ensure-generic-function 'rotation-val :lambda-list '(m))
(cl:defmethod rotation-val ((m <main2nav-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader main_control-srv:rotation-val is deprecated.  Use main_control-srv:rotation instead.")
  (rotation m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <main2nav-request>) ostream)
  "Serializes a message object of type '<main2nav-request>"
  (cl:let* ((signed (cl:slot-value msg 'main_x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'main_y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'rotation)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <main2nav-request>) istream)
  "Deserializes a message object of type '<main2nav-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'main_x) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'main_y) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'rotation) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<main2nav-request>)))
  "Returns string type for a service object of type '<main2nav-request>"
  "main_control/main2navRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'main2nav-request)))
  "Returns string type for a service object of type 'main2nav-request"
  "main_control/main2navRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<main2nav-request>)))
  "Returns md5sum for a message object of type '<main2nav-request>"
  "7efbb833c5f53a4a2e67aab06606b39f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'main2nav-request)))
  "Returns md5sum for a message object of type 'main2nav-request"
  "7efbb833c5f53a4a2e67aab06606b39f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<main2nav-request>)))
  "Returns full string definition for message of type '<main2nav-request>"
  (cl:format cl:nil "int16 main_x~%int16 main_y~%int16 rotation~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'main2nav-request)))
  "Returns full string definition for message of type 'main2nav-request"
  (cl:format cl:nil "int16 main_x~%int16 main_y~%int16 rotation~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <main2nav-request>))
  (cl:+ 0
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <main2nav-request>))
  "Converts a ROS message object to a list"
  (cl:list 'main2nav-request
    (cl:cons ':main_x (main_x msg))
    (cl:cons ':main_y (main_y msg))
    (cl:cons ':rotation (rotation msg))
))
;//! \htmlinclude main2nav-response.msg.html

(cl:defclass <main2nav-response> (roslisp-msg-protocol:ros-message)
  ((done_flag
    :reader done_flag
    :initarg :done_flag
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass main2nav-response (<main2nav-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <main2nav-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'main2nav-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name main_control-srv:<main2nav-response> is deprecated: use main_control-srv:main2nav-response instead.")))

(cl:ensure-generic-function 'done_flag-val :lambda-list '(m))
(cl:defmethod done_flag-val ((m <main2nav-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader main_control-srv:done_flag-val is deprecated.  Use main_control-srv:done_flag instead.")
  (done_flag m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <main2nav-response>) ostream)
  "Serializes a message object of type '<main2nav-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'done_flag) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <main2nav-response>) istream)
  "Deserializes a message object of type '<main2nav-response>"
    (cl:setf (cl:slot-value msg 'done_flag) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<main2nav-response>)))
  "Returns string type for a service object of type '<main2nav-response>"
  "main_control/main2navResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'main2nav-response)))
  "Returns string type for a service object of type 'main2nav-response"
  "main_control/main2navResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<main2nav-response>)))
  "Returns md5sum for a message object of type '<main2nav-response>"
  "7efbb833c5f53a4a2e67aab06606b39f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'main2nav-response)))
  "Returns md5sum for a message object of type 'main2nav-response"
  "7efbb833c5f53a4a2e67aab06606b39f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<main2nav-response>)))
  "Returns full string definition for message of type '<main2nav-response>"
  (cl:format cl:nil "~%bool done_flag~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'main2nav-response)))
  "Returns full string definition for message of type 'main2nav-response"
  (cl:format cl:nil "~%bool done_flag~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <main2nav-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <main2nav-response>))
  "Converts a ROS message object to a list"
  (cl:list 'main2nav-response
    (cl:cons ':done_flag (done_flag msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'main2nav)))
  'main2nav-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'main2nav)))
  'main2nav-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'main2nav)))
  "Returns string type for a service object of type '<main2nav>"
  "main_control/main2nav")