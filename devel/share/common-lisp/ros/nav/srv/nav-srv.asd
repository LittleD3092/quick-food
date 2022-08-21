
(cl:in-package :asdf)

(defsystem "nav-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Service_msg" :depends-on ("_package_Service_msg"))
    (:file "_package_Service_msg" :depends-on ("_package"))
    (:file "main2nav" :depends-on ("_package_main2nav"))
    (:file "_package_main2nav" :depends-on ("_package"))
  ))