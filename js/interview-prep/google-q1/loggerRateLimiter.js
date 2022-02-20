class Logger {
  constructor() {
    this.logs = new Map();
  }

  /**
   *
   * @param {number} timestamp
   * @param {string} message
   * @return {boolean}
   */
  shouldPrintMessage(timestamp, message) {
    if (!this.logs.has(message)) {
      this.logs.set(message, timestamp);
      return true;
    }

    const lastPrinted = this.logs.get(message);

    if (timestamp - lastPrinted < 10) {
      return false;
    }

    this.logs.set(message, timestamp);

    return true;
  }
}