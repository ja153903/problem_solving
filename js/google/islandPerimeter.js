/**
 * @param {number[][]} grid
 * @return {number}
 */
const islandPerimeter = function (grid) {
  if (!grid.length) {
    return 0;
  }

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === 1) {
        return dfs(grid, i, j);
      }
    }
  }

  return 0;
};

/**
  * @param {number[][]} grid
  * @param {number} i
  * @param {number} j
  * @returns {number}
  */
function dfs(grid, i, j) {
  if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length) {
    return 1;
  }

  if (grid[i][j] === 0) {
    return 1;
  }

  if (grid[i][j] === -1) {
    return 0;
  }

  grid[i][j] = -1;

  let count = 0;

  count += dfs(grid, i + 1, j);
  count += dfs(grid, i - 1, j);
  count += dfs(grid, i, j + 1);
  count += dfs(grid, i, j - 1);

  return count;
}

console.log(islandPerimeter([[1,1],[1,1]]));
