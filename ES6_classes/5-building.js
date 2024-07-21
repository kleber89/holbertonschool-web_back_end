class Building {
  constructor(sqft) {
    this._sqft = this._validateNumber(sqft, 'sqft');
    if (new.target === Building) {
      throw new TypeError('Cannot instantiate abstract class Building directly');
    }
  }

  // Validation method
  _validateNumber(value, attribute) {
    if (typeof value !== 'number') {
      throw new TypeError(`${attribute} must be a number`);
    }
    return value;
  }

  // Getter for sqft
  get sqft() {
    return this._sqft;
  }

  // Abstract method
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}

export default Building;
