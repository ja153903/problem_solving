class Logger {
  constructor() {
    this.logs = new Map();
  }

  /**
    * @param {number} timestamp
    * @param {string} message
    * @returns {boolean}
    */
  shouldPrintMessage(timestamp, message) {
    if (!this.logs.has(message)) {
      this.logs.set(message, timestamp);
      return true;
    }

    const lastTimestampPrinted = this.logs.get(message);

    if (timestamp - lastTimestampPrinted >= 10) {
      this.logs.set(message, timestamp);
      return true;
    }

    return false;
  }
}
