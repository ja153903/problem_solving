/**
 * @param {string} rings
 * @return {number}
 */
const countPoints = function (rings) {
  const counter = new Array(10).fill().map(() => ({ R: 0, G: 0, B: 0 }));
  let result = 0;

  for (let i = 0; i < rings.length; i += 2) {
    const ss = rings.substring(i, i + 2);
    const color = ss[0];
    const index = parseInt(ss[1]);

    counter[index][color] += 1;
  }

  for (const { B, G, R } of counter) {
    if (B > 0 && G > 0 && R > 0) {
      result += 1;
    }
  }

  return result;
};

console.log(countPoints("B0B6G0R6R0R6G9"));
