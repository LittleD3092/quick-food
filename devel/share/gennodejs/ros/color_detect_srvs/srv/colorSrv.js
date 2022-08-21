// Auto-generated. Do not edit!

// (in-package color_detect_srvs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class colorSrvRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.position_srv = null;
    }
    else {
      if (initObj.hasOwnProperty('position_srv')) {
        this.position_srv = initObj.position_srv
      }
      else {
        this.position_srv = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type colorSrvRequest
    // Serialize message field [position_srv]
    bufferOffset = _serializer.int16(obj.position_srv, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type colorSrvRequest
    let len;
    let data = new colorSrvRequest(null);
    // Deserialize message field [position_srv]
    data.position_srv = _deserializer.int16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 2;
  }

  static datatype() {
    // Returns string type for a service object
    return 'color_detect_srvs/colorSrvRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3b914a1496294ef741808bfcc7d68343';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16  position_srv
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new colorSrvRequest(null);
    if (msg.position_srv !== undefined) {
      resolved.position_srv = msg.position_srv;
    }
    else {
      resolved.position_srv = 0
    }

    return resolved;
    }
};

class colorSrvResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.color_srv = null;
      this.distance_srv = null;
      this.x_diff_srv = null;
    }
    else {
      if (initObj.hasOwnProperty('color_srv')) {
        this.color_srv = initObj.color_srv
      }
      else {
        this.color_srv = 0;
      }
      if (initObj.hasOwnProperty('distance_srv')) {
        this.distance_srv = initObj.distance_srv
      }
      else {
        this.distance_srv = 0;
      }
      if (initObj.hasOwnProperty('x_diff_srv')) {
        this.x_diff_srv = initObj.x_diff_srv
      }
      else {
        this.x_diff_srv = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type colorSrvResponse
    // Serialize message field [color_srv]
    bufferOffset = _serializer.int16(obj.color_srv, buffer, bufferOffset);
    // Serialize message field [distance_srv]
    bufferOffset = _serializer.int16(obj.distance_srv, buffer, bufferOffset);
    // Serialize message field [x_diff_srv]
    bufferOffset = _serializer.int16(obj.x_diff_srv, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type colorSrvResponse
    let len;
    let data = new colorSrvResponse(null);
    // Deserialize message field [color_srv]
    data.color_srv = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [distance_srv]
    data.distance_srv = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [x_diff_srv]
    data.x_diff_srv = _deserializer.int16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 6;
  }

  static datatype() {
    // Returns string type for a service object
    return 'color_detect_srvs/colorSrvResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4ec7f7dd4aedad819684d04cf6c021e7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    int16 color_srv
    int16 distance_srv
    int16 x_diff_srv
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new colorSrvResponse(null);
    if (msg.color_srv !== undefined) {
      resolved.color_srv = msg.color_srv;
    }
    else {
      resolved.color_srv = 0
    }

    if (msg.distance_srv !== undefined) {
      resolved.distance_srv = msg.distance_srv;
    }
    else {
      resolved.distance_srv = 0
    }

    if (msg.x_diff_srv !== undefined) {
      resolved.x_diff_srv = msg.x_diff_srv;
    }
    else {
      resolved.x_diff_srv = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: colorSrvRequest,
  Response: colorSrvResponse,
  md5sum() { return '8ee3ae6e55f5ddfc2f446e412119bc69'; },
  datatype() { return 'color_detect_srvs/colorSrv'; }
};
