/**
 * @param {string[][]} paths
 * @return {string}
 */
const destCity = function (paths) {
  const dst = new Set();
  const src = new Set();

  for (const [start, end] of paths) {
    dst.add(end);
    src.add(start);
  }

  for (const city of dst) {
    if (!src.has(city)) {
      return city;
    }
  }

  return '';
};
