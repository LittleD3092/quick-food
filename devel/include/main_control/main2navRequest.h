// Generated by gencpp from file main_control/main2navRequest.msg
// DO NOT EDIT!


#ifndef MAIN_CONTROL_MESSAGE_MAIN2NAVREQUEST_H
#define MAIN_CONTROL_MESSAGE_MAIN2NAVREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace main_control
{
template <class ContainerAllocator>
struct main2navRequest_
{
  typedef main2navRequest_<ContainerAllocator> Type;

  main2navRequest_()
    : main_x(0)
    , main_y(0)
    , rotation(0)  {
    }
  main2navRequest_(const ContainerAllocator& _alloc)
    : main_x(0)
    , main_y(0)
    , rotation(0)  {
  (void)_alloc;
    }



   typedef int16_t _main_x_type;
  _main_x_type main_x;

   typedef int16_t _main_y_type;
  _main_y_type main_y;

   typedef int16_t _rotation_type;
  _rotation_type rotation;





  typedef boost::shared_ptr< ::main_control::main2navRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::main_control::main2navRequest_<ContainerAllocator> const> ConstPtr;

}; // struct main2navRequest_

typedef ::main_control::main2navRequest_<std::allocator<void> > main2navRequest;

typedef boost::shared_ptr< ::main_control::main2navRequest > main2navRequestPtr;
typedef boost::shared_ptr< ::main_control::main2navRequest const> main2navRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::main_control::main2navRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::main_control::main2navRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::main_control::main2navRequest_<ContainerAllocator1> & lhs, const ::main_control::main2navRequest_<ContainerAllocator2> & rhs)
{
  return lhs.main_x == rhs.main_x &&
    lhs.main_y == rhs.main_y &&
    lhs.rotation == rhs.rotation;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::main_control::main2navRequest_<ContainerAllocator1> & lhs, const ::main_control::main2navRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace main_control

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::main_control::main2navRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::main_control::main2navRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::main_control::main2navRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::main_control::main2navRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::main_control::main2navRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::main_control::main2navRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::main_control::main2navRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f843328f83790b38c3605d91a07665a8";
  }

  static const char* value(const ::main_control::main2navRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf843328f83790b38ULL;
  static const uint64_t static_value2 = 0xc3605d91a07665a8ULL;
};

template<class ContainerAllocator>
struct DataType< ::main_control::main2navRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "main_control/main2navRequest";
  }

  static const char* value(const ::main_control::main2navRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::main_control::main2navRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int16 main_x\n"
"int16 main_y\n"
"int16 rotation\n"
"\n"
;
  }

  static const char* value(const ::main_control::main2navRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::main_control::main2navRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.main_x);
      stream.next(m.main_y);
      stream.next(m.rotation);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct main2navRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::main_control::main2navRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::main_control::main2navRequest_<ContainerAllocator>& v)
  {
    s << indent << "main_x: ";
    Printer<int16_t>::stream(s, indent + "  ", v.main_x);
    s << indent << "main_y: ";
    Printer<int16_t>::stream(s, indent + "  ", v.main_y);
    s << indent << "rotation: ";
    Printer<int16_t>::stream(s, indent + "  ", v.rotation);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MAIN_CONTROL_MESSAGE_MAIN2NAVREQUEST_H
