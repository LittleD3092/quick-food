;; Auto-generated. Do not edit!


(when (boundp 'color_detect_srvs::colorSrv)
  (if (not (find-package "COLOR_DETECT_SRVS"))
    (make-package "COLOR_DETECT_SRVS"))
  (shadow 'colorSrv (find-package "COLOR_DETECT_SRVS")))
(unless (find-package "COLOR_DETECT_SRVS::COLORSRV")
  (make-package "COLOR_DETECT_SRVS::COLORSRV"))
(unless (find-package "COLOR_DETECT_SRVS::COLORSRVREQUEST")
  (make-package "COLOR_DETECT_SRVS::COLORSRVREQUEST"))
(unless (find-package "COLOR_DETECT_SRVS::COLORSRVRESPONSE")
  (make-package "COLOR_DETECT_SRVS::COLORSRVRESPONSE"))

(in-package "ROS")





(defclass color_detect_srvs::colorSrvRequest
  :super ros::object
  :slots (_position_srv ))

(defmethod color_detect_srvs::colorSrvRequest
  (:init
   (&key
    ((:position_srv __position_srv) 0)
    )
   (send-super :init)
   (setq _position_srv (round __position_srv))
   self)
  (:position_srv
   (&optional __position_srv)
   (if __position_srv (setq _position_srv __position_srv)) _position_srv)
  (:serialization-length
   ()
   (+
    ;; int16 _position_srv
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _position_srv
       (write-word _position_srv s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _position_srv
     (setq _position_srv (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(defclass color_detect_srvs::colorSrvResponse
  :super ros::object
  :slots (_color_srv _distance_srv _x_diff_srv ))

(defmethod color_detect_srvs::colorSrvResponse
  (:init
   (&key
    ((:color_srv __color_srv) 0)
    ((:distance_srv __distance_srv) 0)
    ((:x_diff_srv __x_diff_srv) 0)
    )
   (send-super :init)
   (setq _color_srv (round __color_srv))
   (setq _distance_srv (round __distance_srv))
   (setq _x_diff_srv (round __x_diff_srv))
   self)
  (:color_srv
   (&optional __color_srv)
   (if __color_srv (setq _color_srv __color_srv)) _color_srv)
  (:distance_srv
   (&optional __distance_srv)
   (if __distance_srv (setq _distance_srv __distance_srv)) _distance_srv)
  (:x_diff_srv
   (&optional __x_diff_srv)
   (if __x_diff_srv (setq _x_diff_srv __x_diff_srv)) _x_diff_srv)
  (:serialization-length
   ()
   (+
    ;; int16 _color_srv
    2
    ;; int16 _distance_srv
    2
    ;; int16 _x_diff_srv
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _color_srv
       (write-word _color_srv s)
     ;; int16 _distance_srv
       (write-word _distance_srv s)
     ;; int16 _x_diff_srv
       (write-word _x_diff_srv s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _color_srv
     (setq _color_srv (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _distance_srv
     (setq _distance_srv (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _x_diff_srv
     (setq _x_diff_srv (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(defclass color_detect_srvs::colorSrv
  :super ros::object
  :slots ())

(setf (get color_detect_srvs::colorSrv :md5sum-) "8ee3ae6e55f5ddfc2f446e412119bc69")
(setf (get color_detect_srvs::colorSrv :datatype-) "color_detect_srvs/colorSrv")
(setf (get color_detect_srvs::colorSrv :request) color_detect_srvs::colorSrvRequest)
(setf (get color_detect_srvs::colorSrv :response) color_detect_srvs::colorSrvResponse)

(defmethod color_detect_srvs::colorSrvRequest
  (:response () (instance color_detect_srvs::colorSrvResponse :init)))

(setf (get color_detect_srvs::colorSrvRequest :md5sum-) "8ee3ae6e55f5ddfc2f446e412119bc69")
(setf (get color_detect_srvs::colorSrvRequest :datatype-) "color_detect_srvs/colorSrvRequest")
(setf (get color_detect_srvs::colorSrvRequest :definition-)
      "int16  position_srv

---

int16 color_srv
int16 distance_srv
int16 x_diff_srv

")

(setf (get color_detect_srvs::colorSrvResponse :md5sum-) "8ee3ae6e55f5ddfc2f446e412119bc69")
(setf (get color_detect_srvs::colorSrvResponse :datatype-) "color_detect_srvs/colorSrvResponse")
(setf (get color_detect_srvs::colorSrvResponse :definition-)
      "int16  position_srv

---

int16 color_srv
int16 distance_srv
int16 x_diff_srv

")



(provide :color_detect_srvs/colorSrv "8ee3ae6e55f5ddfc2f446e412119bc69")


