/* Auto-generated by genmsg_cpp for file /home/ahmed/me597/ROS_packages/clearpath_horizon/msg/SystemStatus.msg */
#ifndef CLEARPATH_HORIZON_MESSAGE_SYSTEMSTATUS_H
#define CLEARPATH_HORIZON_MESSAGE_SYSTEMSTATUS_H
#include <string>
#include <vector>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/message.h"
#include "ros/time.h"

#include "std_msgs/Header.h"

namespace clearpath_horizon
{
template <class ContainerAllocator>
struct SystemStatus_ : public ros::Message
{
  typedef SystemStatus_<ContainerAllocator> Type;

  SystemStatus_()
  : header()
  , uptime(0)
  , voltages()
  , currents()
  , temperatures()
  {
  }

  SystemStatus_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , uptime(0)
  , voltages(_alloc)
  , currents(_alloc)
  , temperatures(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef uint32_t _uptime_type;
  uint32_t uptime;

  typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _voltages_type;
  std::vector<double, typename ContainerAllocator::template rebind<double>::other >  voltages;

  typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _currents_type;
  std::vector<double, typename ContainerAllocator::template rebind<double>::other >  currents;

  typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _temperatures_type;
  std::vector<double, typename ContainerAllocator::template rebind<double>::other >  temperatures;


  ROS_DEPRECATED uint32_t get_voltages_size() const { return (uint32_t)voltages.size(); }
  ROS_DEPRECATED void set_voltages_size(uint32_t size) { voltages.resize((size_t)size); }
  ROS_DEPRECATED void get_voltages_vec(std::vector<double, typename ContainerAllocator::template rebind<double>::other > & vec) const { vec = this->voltages; }
  ROS_DEPRECATED void set_voltages_vec(const std::vector<double, typename ContainerAllocator::template rebind<double>::other > & vec) { this->voltages = vec; }
  ROS_DEPRECATED uint32_t get_currents_size() const { return (uint32_t)currents.size(); }
  ROS_DEPRECATED void set_currents_size(uint32_t size) { currents.resize((size_t)size); }
  ROS_DEPRECATED void get_currents_vec(std::vector<double, typename ContainerAllocator::template rebind<double>::other > & vec) const { vec = this->currents; }
  ROS_DEPRECATED void set_currents_vec(const std::vector<double, typename ContainerAllocator::template rebind<double>::other > & vec) { this->currents = vec; }
  ROS_DEPRECATED uint32_t get_temperatures_size() const { return (uint32_t)temperatures.size(); }
  ROS_DEPRECATED void set_temperatures_size(uint32_t size) { temperatures.resize((size_t)size); }
  ROS_DEPRECATED void get_temperatures_vec(std::vector<double, typename ContainerAllocator::template rebind<double>::other > & vec) const { vec = this->temperatures; }
  ROS_DEPRECATED void set_temperatures_vec(const std::vector<double, typename ContainerAllocator::template rebind<double>::other > & vec) { this->temperatures = vec; }
private:
  static const char* __s_getDataType_() { return "clearpath_horizon/SystemStatus"; }
public:
  ROS_DEPRECATED static const std::string __s_getDataType() { return __s_getDataType_(); }

  ROS_DEPRECATED const std::string __getDataType() const { return __s_getDataType_(); }

private:
  static const char* __s_getMD5Sum_() { return "b24850c808eb727058fff35ba598006f"; }
public:
  ROS_DEPRECATED static const std::string __s_getMD5Sum() { return __s_getMD5Sum_(); }

  ROS_DEPRECATED const std::string __getMD5Sum() const { return __s_getMD5Sum_(); }

private:
  static const char* __s_getMessageDefinition_() { return "Header header\n\
uint32 uptime\n\
float64[] voltages\n\
float64[] currents\n\
float64[] temperatures\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
"; }
public:
  ROS_DEPRECATED static const std::string __s_getMessageDefinition() { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED const std::string __getMessageDefinition() const { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED virtual uint8_t *serialize(uint8_t *write_ptr, uint32_t seq) const
  {
    ros::serialization::OStream stream(write_ptr, 1000000000);
    ros::serialization::serialize(stream, header);
    ros::serialization::serialize(stream, uptime);
    ros::serialization::serialize(stream, voltages);
    ros::serialization::serialize(stream, currents);
    ros::serialization::serialize(stream, temperatures);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    ros::serialization::IStream stream(read_ptr, 1000000000);
    ros::serialization::deserialize(stream, header);
    ros::serialization::deserialize(stream, uptime);
    ros::serialization::deserialize(stream, voltages);
    ros::serialization::deserialize(stream, currents);
    ros::serialization::deserialize(stream, temperatures);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint32_t serializationLength() const
  {
    uint32_t size = 0;
    size += ros::serialization::serializationLength(header);
    size += ros::serialization::serializationLength(uptime);
    size += ros::serialization::serializationLength(voltages);
    size += ros::serialization::serializationLength(currents);
    size += ros::serialization::serializationLength(temperatures);
    return size;
  }

  typedef boost::shared_ptr< ::clearpath_horizon::SystemStatus_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::clearpath_horizon::SystemStatus_<ContainerAllocator>  const> ConstPtr;
}; // struct SystemStatus
typedef  ::clearpath_horizon::SystemStatus_<std::allocator<void> > SystemStatus;

typedef boost::shared_ptr< ::clearpath_horizon::SystemStatus> SystemStatusPtr;
typedef boost::shared_ptr< ::clearpath_horizon::SystemStatus const> SystemStatusConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::clearpath_horizon::SystemStatus_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::clearpath_horizon::SystemStatus_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace clearpath_horizon

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator>
struct MD5Sum< ::clearpath_horizon::SystemStatus_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b24850c808eb727058fff35ba598006f";
  }

  static const char* value(const  ::clearpath_horizon::SystemStatus_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xb24850c808eb7270ULL;
  static const uint64_t static_value2 = 0x58fff35ba598006fULL;
};

template<class ContainerAllocator>
struct DataType< ::clearpath_horizon::SystemStatus_<ContainerAllocator> > {
  static const char* value() 
  {
    return "clearpath_horizon/SystemStatus";
  }

  static const char* value(const  ::clearpath_horizon::SystemStatus_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::clearpath_horizon::SystemStatus_<ContainerAllocator> > {
  static const char* value() 
  {
    return "Header header\n\
uint32 uptime\n\
float64[] voltages\n\
float64[] currents\n\
float64[] temperatures\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
";
  }

  static const char* value(const  ::clearpath_horizon::SystemStatus_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::clearpath_horizon::SystemStatus_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::clearpath_horizon::SystemStatus_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::clearpath_horizon::SystemStatus_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.uptime);
    stream.next(m.voltages);
    stream.next(m.currents);
    stream.next(m.temperatures);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct SystemStatus_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::clearpath_horizon::SystemStatus_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::clearpath_horizon::SystemStatus_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "uptime: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.uptime);
    s << indent << "voltages[]" << std::endl;
    for (size_t i = 0; i < v.voltages.size(); ++i)
    {
      s << indent << "  voltages[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.voltages[i]);
    }
    s << indent << "currents[]" << std::endl;
    for (size_t i = 0; i < v.currents.size(); ++i)
    {
      s << indent << "  currents[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.currents[i]);
    }
    s << indent << "temperatures[]" << std::endl;
    for (size_t i = 0; i < v.temperatures.size(); ++i)
    {
      s << indent << "  temperatures[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.temperatures[i]);
    }
  }
};


} // namespace message_operations
} // namespace ros

#endif // CLEARPATH_HORIZON_MESSAGE_SYSTEMSTATUS_H

