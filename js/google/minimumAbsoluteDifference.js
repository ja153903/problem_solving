/**
 * @param {number[]} arr
 * @return {number[][]}
 */
const minimumAbsDifference = function (arr) {
  let minAbsDiff = Number.MAX_SAFE_INTEGER;
  const sortedArr = arr.sort((a, b) => a - b);

  for (let i = 1; i < sortedArr.length; i++) {
    minAbsDiff = Math.min(minAbsDiff, sortedArr[i] - sortedArr[i - 1]);
  }

  const result = [];

  for (let i = 1; i < sortedArr.length; i++) {
    if (sortedArr[i] - sortedArr[i - 1] === minAbsDiff) {
      result.push([sortedArr[i - 1], sortedArr[i]]);
    }
  }

  return result;
};