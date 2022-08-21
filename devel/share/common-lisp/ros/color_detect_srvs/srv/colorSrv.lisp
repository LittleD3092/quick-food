; Auto-generated. Do not edit!


(cl:in-package color_detect_srvs-srv)


;//! \htmlinclude colorSrv-request.msg.html

(cl:defclass <colorSrv-request> (roslisp-msg-protocol:ros-message)
  ((position_srv
    :reader position_srv
    :initarg :position_srv
    :type cl:fixnum
    :initform 0))
)

(cl:defclass colorSrv-request (<colorSrv-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <colorSrv-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'colorSrv-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name color_detect_srvs-srv:<colorSrv-request> is deprecated: use color_detect_srvs-srv:colorSrv-request instead.")))

(cl:ensure-generic-function 'position_srv-val :lambda-list '(m))
(cl:defmethod position_srv-val ((m <colorSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader color_detect_srvs-srv:position_srv-val is deprecated.  Use color_detect_srvs-srv:position_srv instead.")
  (position_srv m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <colorSrv-request>) ostream)
  "Serializes a message object of type '<colorSrv-request>"
  (cl:let* ((signed (cl:slot-value msg 'position_srv)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <colorSrv-request>) istream)
  "Deserializes a message object of type '<colorSrv-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'position_srv) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<colorSrv-request>)))
  "Returns string type for a service object of type '<colorSrv-request>"
  "color_detect_srvs/colorSrvRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'colorSrv-request)))
  "Returns string type for a service object of type 'colorSrv-request"
  "color_detect_srvs/colorSrvRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<colorSrv-request>)))
  "Returns md5sum for a message object of type '<colorSrv-request>"
  "8ee3ae6e55f5ddfc2f446e412119bc69")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'colorSrv-request)))
  "Returns md5sum for a message object of type 'colorSrv-request"
  "8ee3ae6e55f5ddfc2f446e412119bc69")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<colorSrv-request>)))
  "Returns full string definition for message of type '<colorSrv-request>"
  (cl:format cl:nil "int16  position_srv~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'colorSrv-request)))
  "Returns full string definition for message of type 'colorSrv-request"
  (cl:format cl:nil "int16  position_srv~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <colorSrv-request>))
  (cl:+ 0
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <colorSrv-request>))
  "Converts a ROS message object to a list"
  (cl:list 'colorSrv-request
    (cl:cons ':position_srv (position_srv msg))
))
;//! \htmlinclude colorSrv-response.msg.html

(cl:defclass <colorSrv-response> (roslisp-msg-protocol:ros-message)
  ((color_srv
    :reader color_srv
    :initarg :color_srv
    :type cl:fixnum
    :initform 0)
   (distance_srv
    :reader distance_srv
    :initarg :distance_srv
    :type cl:fixnum
    :initform 0)
   (x_diff_srv
    :reader x_diff_srv
    :initarg :x_diff_srv
    :type cl:fixnum
    :initform 0))
)

(cl:defclass colorSrv-response (<colorSrv-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <colorSrv-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'colorSrv-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name color_detect_srvs-srv:<colorSrv-response> is deprecated: use color_detect_srvs-srv:colorSrv-response instead.")))

(cl:ensure-generic-function 'color_srv-val :lambda-list '(m))
(cl:defmethod color_srv-val ((m <colorSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader color_detect_srvs-srv:color_srv-val is deprecated.  Use color_detect_srvs-srv:color_srv instead.")
  (color_srv m))

(cl:ensure-generic-function 'distance_srv-val :lambda-list '(m))
(cl:defmethod distance_srv-val ((m <colorSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader color_detect_srvs-srv:distance_srv-val is deprecated.  Use color_detect_srvs-srv:distance_srv instead.")
  (distance_srv m))

(cl:ensure-generic-function 'x_diff_srv-val :lambda-list '(m))
(cl:defmethod x_diff_srv-val ((m <colorSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader color_detect_srvs-srv:x_diff_srv-val is deprecated.  Use color_detect_srvs-srv:x_diff_srv instead.")
  (x_diff_srv m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <colorSrv-response>) ostream)
  "Serializes a message object of type '<colorSrv-response>"
  (cl:let* ((signed (cl:slot-value msg 'color_srv)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'distance_srv)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'x_diff_srv)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <colorSrv-response>) istream)
  "Deserializes a message object of type '<colorSrv-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'color_srv) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'distance_srv) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x_diff_srv) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<colorSrv-response>)))
  "Returns string type for a service object of type '<colorSrv-response>"
  "color_detect_srvs/colorSrvResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'colorSrv-response)))
  "Returns string type for a service object of type 'colorSrv-response"
  "color_detect_srvs/colorSrvResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<colorSrv-response>)))
  "Returns md5sum for a message object of type '<colorSrv-response>"
  "8ee3ae6e55f5ddfc2f446e412119bc69")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'colorSrv-response)))
  "Returns md5sum for a message object of type 'colorSrv-response"
  "8ee3ae6e55f5ddfc2f446e412119bc69")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<colorSrv-response>)))
  "Returns full string definition for message of type '<colorSrv-response>"
  (cl:format cl:nil "~%int16 color_srv~%int16 distance_srv~%int16 x_diff_srv~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'colorSrv-response)))
  "Returns full string definition for message of type 'colorSrv-response"
  (cl:format cl:nil "~%int16 color_srv~%int16 distance_srv~%int16 x_diff_srv~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <colorSrv-response>))
  (cl:+ 0
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <colorSrv-response>))
  "Converts a ROS message object to a list"
  (cl:list 'colorSrv-response
    (cl:cons ':color_srv (color_srv msg))
    (cl:cons ':distance_srv (distance_srv msg))
    (cl:cons ':x_diff_srv (x_diff_srv msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'colorSrv)))
  'colorSrv-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'colorSrv)))
  'colorSrv-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'colorSrv)))
  "Returns string type for a service object of type '<colorSrv>"
  "color_detect_srvs/colorSrv")