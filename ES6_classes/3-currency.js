class Currency {
  constructor(code, name) {
    this._code = this._validateString(code, 'code');
    this._name = this._validateString(name, 'name');
  }

  // Getter and setter for code
  get code() {
    return this._code;
  }

  set code(value) {
    this._code = this._validateString(value, 'code');
  }

  // Getter and setter for name
  get name() {
    return this._name;
  }

  set name(value) {
    this._name = this._validateString(value, 'name');
  }

  // Method to display full currency
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}

export default Currency;
