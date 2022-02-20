/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} indices
 * @return {number}
 */
const oddCells = function (m, n, indices) {
  const matrix = new Array(m);
  for (let i = 0; i < m; i++) {
    matrix[i] = new Array(n).fill(0);
  }

  for (const [row, col] of indices) {
    for (let i = 0; i < n; i++) {
      matrix[row][i]++;
    }

    for (let i = 0; i < m; i++) {
      matrix[i][col]++;
    }
  }

  console.log(matrix)

  return matrix.reduce((acc, row) => {
    return acc + row.reduce((acc, col) => {
      if (col % 2 === 0) {
        return acc;
      }

      return acc + 1;
    }, 0)
  }, 0);
};

console.log(oddCells(2, 3, [[0, 1], [1, 1]]));