/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} indices
 * @return {number}
 */
const oddCells = function (m, n, indices) {
  const matrix = [];
  for (let i = 0; i < m; i++) {
    matrix.push(new Array(n).fill(0));
  }

  for (const [row, col] of indices) {
    for (let i = 0; i < n; i++) {
      matrix[row][i] += 1;
    }

    for (let i = 0; i < m; i++) {
      matrix[i][col] += 1;
    }
  }

  return matrix.reduce((sum, row) => {
    return sum + row.reduce((acc, col) => {
      if (col % 2 === 1) {
        return acc + 1;
      } else {
        return acc;
      }
    }, 0);
  }, 0);
};

console.log(oddCells(
  2, 2, [[1,1],[0,0]]
));
