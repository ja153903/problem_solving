/**
 * === Approach ===
 * Note that the maximum amount we can increase a building by cannot exceed the maximum value
 * in that row or that column
 *
 * @param {number[][]} grid
 * @return {number}
 */
const maxIncreaseKeepingSkyline = function (grid) {
  const rows = new Array(grid.length).fill(0);
  const cols = new Array(grid[0].length).fill(0);

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      rows[i] = Math.max(rows[i], grid[i][j]);
      cols[j] = Math.max(cols[j], grid[i][j]);
    }
  }

  let res = 0;

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      res += Math.min(rows[i], cols[j]) - grid[i][j];
    }
  }

  return res;
};
