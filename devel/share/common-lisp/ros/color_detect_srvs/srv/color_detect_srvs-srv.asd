
(cl:in-package :asdf)

(defsystem "color_detect_srvs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "colorSrv" :depends-on ("_package_colorSrv"))
    (:file "_package_colorSrv" :depends-on ("_package"))
  ))