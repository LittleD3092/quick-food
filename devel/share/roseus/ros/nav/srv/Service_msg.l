;; Auto-generated. Do not edit!


(when (boundp 'nav::Service_msg)
  (if (not (find-package "NAV"))
    (make-package "NAV"))
  (shadow 'Service_msg (find-package "NAV")))
(unless (find-package "NAV::SERVICE_MSG")
  (make-package "NAV::SERVICE_MSG"))
(unless (find-package "NAV::SERVICE_MSGREQUEST")
  (make-package "NAV::SERVICE_MSGREQUEST"))
(unless (find-package "NAV::SERVICE_MSGRESPONSE")
  (make-package "NAV::SERVICE_MSGRESPONSE"))

(in-package "ROS")





(defclass nav::Service_msgRequest
  :super ros::object
  :slots (_direction _velocity _rotation ))

(defmethod nav::Service_msgRequest
  (:init
   (&key
    ((:direction __direction) 0)
    ((:velocity __velocity) 0)
    ((:rotation __rotation) 0)
    )
   (send-super :init)
   (setq _direction (round __direction))
   (setq _velocity (round __velocity))
   (setq _rotation (round __rotation))
   self)
  (:direction
   (&optional __direction)
   (if __direction (setq _direction __direction)) _direction)
  (:velocity
   (&optional __velocity)
   (if __velocity (setq _velocity __velocity)) _velocity)
  (:rotation
   (&optional __rotation)
   (if __rotation (setq _rotation __rotation)) _rotation)
  (:serialization-length
   ()
   (+
    ;; int16 _direction
    2
    ;; int16 _velocity
    2
    ;; int16 _rotation
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _direction
       (write-word _direction s)
     ;; int16 _velocity
       (write-word _velocity s)
     ;; int16 _rotation
       (write-word _rotation s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _direction
     (setq _direction (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _velocity
     (setq _velocity (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _rotation
     (setq _rotation (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(defclass nav::Service_msgResponse
  :super ros::object
  :slots (_receive_data ))

(defmethod nav::Service_msgResponse
  (:init
   (&key
    ((:receive_data __receive_data) nil)
    )
   (send-super :init)
   (setq _receive_data __receive_data)
   self)
  (:receive_data
   (&optional (__receive_data :null))
   (if (not (eq __receive_data :null)) (setq _receive_data __receive_data)) _receive_data)
  (:serialization-length
   ()
   (+
    ;; bool _receive_data
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _receive_data
       (if _receive_data (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _receive_data
     (setq _receive_data (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass nav::Service_msg
  :super ros::object
  :slots ())

(setf (get nav::Service_msg :md5sum-) "86301fa8233c7fe1657e8060a290c050")
(setf (get nav::Service_msg :datatype-) "nav/Service_msg")
(setf (get nav::Service_msg :request) nav::Service_msgRequest)
(setf (get nav::Service_msg :response) nav::Service_msgResponse)

(defmethod nav::Service_msgRequest
  (:response () (instance nav::Service_msgResponse :init)))

(setf (get nav::Service_msgRequest :md5sum-) "86301fa8233c7fe1657e8060a290c050")
(setf (get nav::Service_msgRequest :datatype-) "nav/Service_msgRequest")
(setf (get nav::Service_msgRequest :definition-)
      "int16 direction
int16 velocity
int16 rotation
---
bool receive_data

")

(setf (get nav::Service_msgResponse :md5sum-) "86301fa8233c7fe1657e8060a290c050")
(setf (get nav::Service_msgResponse :datatype-) "nav/Service_msgResponse")
(setf (get nav::Service_msgResponse :definition-)
      "int16 direction
int16 velocity
int16 rotation
---
bool receive_data

")



(provide :nav/Service_msg "86301fa8233c7fe1657e8060a290c050")


