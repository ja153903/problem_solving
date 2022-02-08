/**
 * TODO: Did not finish this problem
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {string}
 */
const longestDiverseString = function (a, b, c) {
  const maxLen = a + b + c;
  const result = new Array(maxLen).fill("*");

  const values = [
    { value: "a", count: a },
    { value: "b", count: b },
    { value: "c", count: c },
  ];
  values.sort((a, b) => b.count - a.count);

  let j = 0;

  for (const { value, count } of values) {
    let i = 0;

    while (i < count) {
      if (j >= maxLen) {
        break;
      }

      if (
        j >= 2 &&
        result[j - 2] === result[j - 1] &&
        value === result[j - 1]
      ) {
        // if the previous two indices were the same,
        // then we should update j
        j += 1;
        continue;
      }

      result[j] = value;
      j += 1;
      i += 1;
    }

    for (let i = 0; i < result.length; i++) {
      if (result[i] === "*") {
        j = i;
        break;
      }
    }
  }

  return result.filter((ch) => ch !== "*").join("");
};

//console.log(longestDiverseString(1, 1, 7));
console.log(longestDiverseString(7, 1, 0));
