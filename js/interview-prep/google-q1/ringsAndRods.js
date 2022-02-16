/**
 * @param {string} rings
 * @return {number}
 */
const countPoints = function (rings) {
  const counter = { R: 0, G: 0, B: 0 };
  const arr = new Array(10);
  for (let i = 0; i < 10; i++) {
    arr[i] = { ...counter };
  }

  for (let i = 0; i < rings.length; i += 2) {
    const color = rings[i];
    const point = parseInt(rings[i + 1]);
    arr[point][color]++;
  }

  return arr.reduce((acc, curr) => {
    if (curr['R'] > 0 && curr['G'] > 0 && curr['B'] > 0) {
      return acc + 1;
    }

    return acc;
  }, 0);
};

console.log(countPoints('G4'))
console.log(countPoints("B7R5B3G5B1R2B8"))
console.log(countPoints("G7G9R4B0G6R1R9R5B8R4G4B4R6B4B1G2B9G5B6G5"))