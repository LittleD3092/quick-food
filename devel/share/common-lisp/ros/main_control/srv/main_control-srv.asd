
(cl:in-package :asdf)

(defsystem "main_control-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "main2nav" :depends-on ("_package_main2nav"))
    (:file "_package_main2nav" :depends-on ("_package"))
  ))