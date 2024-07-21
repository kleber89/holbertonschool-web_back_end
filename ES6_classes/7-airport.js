class Airport {
  constructor(name, code) {
    this._name = this._validateString(name, 'name');
    this._code = this._validateString(code, 'code');
  }

  // Validation method
  _validateString(value, attribute) {
    if (typeof value !== 'string') {
      throw new TypeError(`${attribute} must be a string`);
    }
    return value;
  }

  // Getter and setter for name
  get name() {
    return this._name;
  }

  set name(value) {
    this._name = this._validateString(value, 'name');
  }

  // Getter and setter for code
  get code() {
    return this._code;
  }

  set code(value) {
    this._code = this._validateString(value, 'code');
  }

  // Override toString method
  toString() {
    return this._code;
  }
}

export default Airport;
