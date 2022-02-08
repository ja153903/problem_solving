/**
 * @param {number} num
 * @return {number}
 */
const addDigits = function(num) {
  let n = 0;

  while (true) {
    while (num > 0) {
      n += num % 10;
      num = Math.floor(num / 10);
    }

    if (n < 10) {
      break;
    }

    num = n;
    n = 0;
  }

  return n;
};

console.log(addDigits(38));
