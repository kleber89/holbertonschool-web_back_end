import Currency from './3-currency.js';

class Pricing {
  constructor(amount, currency) {
    this._amount = this._validateNumber(amount, 'amount');
    this._currency = this._validateCurrency(currency, 'currency');
  }

  // Validation methods
  _validateNumber(value, attribute) {
    if (typeof value !== 'number') {
      throw new TypeError(`${attribute} must be a number`);
    }
    return value;
  }

  _validateCurrency(value, attribute) {
    if (!(value instanceof Currency)) {
      throw new TypeError(`${attribute} must be an instance of Currency`);
    }
    return value;
  }

  // Getter and setter for amount
  get amount() {
    return this._amount;
  }

  set amount(value) {
    this._amount = this._validateNumber(value, 'amount');
  }

  // Getter and setter for currency
  get currency() {
    return this._currency;
  }

  set currency(value) {
    this._currency = this._validateCurrency(value, 'currency');
  }

  // Method to display full price
  displayFullPrice() {
    return `${this._amount} ${this._currency.displayFullCurrency()}`;
  }

  // Static method to convert price
  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('Both amount and conversionRate must be numbers');
    }
    return amount * conversionRate;
  }
}

export default Pricing;
