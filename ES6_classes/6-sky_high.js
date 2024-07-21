import Building from './5-building.js';

class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft); // Assign sqft to the parent class Building
    this._floors = this._validateNumber(floors, 'floors'); // Validate and assign floors
  }

  // Getter for floors
  get floors() {
    return this._floors;
  }

  // Overriding the abstract method
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors.`;
  }
}

export default SkyHighBuilding;
