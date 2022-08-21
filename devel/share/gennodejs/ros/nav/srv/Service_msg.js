// Auto-generated. Do not edit!

// (in-package nav.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class Service_msgRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.direction = null;
      this.velocity = null;
      this.rotation = null;
    }
    else {
      if (initObj.hasOwnProperty('direction')) {
        this.direction = initObj.direction
      }
      else {
        this.direction = 0;
      }
      if (initObj.hasOwnProperty('velocity')) {
        this.velocity = initObj.velocity
      }
      else {
        this.velocity = 0;
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
    // Serializes a message object of type Service_msgRequest
    // Serialize message field [direction]
    bufferOffset = _serializer.int16(obj.direction, buffer, bufferOffset);
    // Serialize message field [velocity]
    bufferOffset = _serializer.int16(obj.velocity, buffer, bufferOffset);
    // Serialize message field [rotation]
    bufferOffset = _serializer.int16(obj.rotation, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Service_msgRequest
    let len;
    let data = new Service_msgRequest(null);
    // Deserialize message field [direction]
    data.direction = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [velocity]
    data.velocity = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [rotation]
    data.rotation = _deserializer.int16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 6;
  }

  static datatype() {
    // Returns string type for a service object
    return 'nav/Service_msgRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '717d6bf27c8d24b77022a79e91c76f8e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16 direction
    int16 velocity
    int16 rotation
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Service_msgRequest(null);
    if (msg.direction !== undefined) {
      resolved.direction = msg.direction;
    }
    else {
      resolved.direction = 0
    }

    if (msg.velocity !== undefined) {
      resolved.velocity = msg.velocity;
    }
    else {
      resolved.velocity = 0
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

class Service_msgResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.receive_data = null;
    }
    else {
      if (initObj.hasOwnProperty('receive_data')) {
        this.receive_data = initObj.receive_data
      }
      else {
        this.receive_data = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Service_msgResponse
    // Serialize message field [receive_data]
    bufferOffset = _serializer.bool(obj.receive_data, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Service_msgResponse
    let len;
    let data = new Service_msgResponse(null);
    // Deserialize message field [receive_data]
    data.receive_data = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'nav/Service_msgResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '27168afa375534d85a68932f3fe53718';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool receive_data
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Service_msgResponse(null);
    if (msg.receive_data !== undefined) {
      resolved.receive_data = msg.receive_data;
    }
    else {
      resolved.receive_data = false
    }

    return resolved;
    }
};

module.exports = {
  Request: Service_msgRequest,
  Response: Service_msgResponse,
  md5sum() { return '86301fa8233c7fe1657e8060a290c050'; },
  datatype() { return 'nav/Service_msg'; }
};
