// Auto-generated. Do not edit!

// (in-package main_control.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class main2navRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.main_x = null;
      this.main_y = null;
      this.rotation = null;
    }
    else {
      if (initObj.hasOwnProperty('main_x')) {
        this.main_x = initObj.main_x
      }
      else {
        this.main_x = 0;
      }
      if (initObj.hasOwnProperty('main_y')) {
        this.main_y = initObj.main_y
      }
      else {
        this.main_y = 0;
      }
      if (initObj.hasOwnProperty('rotation')) {
        this.rotation = initObj.rotation
      }
      else {
        this.rotation = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type main2navRequest
    // Serialize message field [main_x]
    bufferOffset = _serializer.int16(obj.main_x, buffer, bufferOffset);
    // Serialize message field [main_y]
    bufferOffset = _serializer.int16(obj.main_y, buffer, bufferOffset);
    // Serialize message field [rotation]
    bufferOffset = _serializer.int16(obj.rotation, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type main2navRequest
    let len;
    let data = new main2navRequest(null);
    // Deserialize message field [main_x]
    data.main_x = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [main_y]
    data.main_y = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [rotation]
    data.rotation = _deserializer.int16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 6;
  }

  static datatype() {
    // Returns string type for a service object
    return 'main_control/main2navRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f843328f83790b38c3605d91a07665a8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16 main_x
    int16 main_y
    int16 rotation
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new main2navRequest(null);
    if (msg.main_x !== undefined) {
      resolved.main_x = msg.main_x;
    }
    else {
      resolved.main_x = 0
    }

    if (msg.main_y !== undefined) {
      resolved.main_y = msg.main_y;
    }
    else {
      resolved.main_y = 0
    }

    if (msg.rotation !== undefined) {
      resolved.rotation = msg.rotation;
    }
    else {
      resolved.rotation = 0
    }

    return resolved;
    }
};

class main2navResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.done_flag = null;
    }
    else {
      if (initObj.hasOwnProperty('done_flag')) {
        this.done_flag = initObj.done_flag
      }
      else {
        this.done_flag = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type main2navResponse
    // Serialize message field [done_flag]
    bufferOffset = _serializer.bool(obj.done_flag, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type main2navResponse
    let len;
    let data = new main2navResponse(null);
    // Deserialize message field [done_flag]
    data.done_flag = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'main_control/main2navResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '02525f6b4e1610a0b6835d9d8e696b93';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    bool done_flag
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new main2navResponse(null);
    if (msg.done_flag !== undefined) {
      resolved.done_flag = msg.done_flag;
    }
    else {
      resolved.done_flag = false
    }

    return resolved;
    }
};

module.exports = {
  Request: main2navRequest,
  Response: main2navResponse,
  md5sum() { return '7efbb833c5f53a4a2e67aab06606b39f'; },
  datatype() { return 'main_control/main2nav'; }
};
