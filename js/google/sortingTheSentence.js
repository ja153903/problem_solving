/**
 * @param {string} s
 * @returns {string}
 */
function sortSentence(s) {
  const words = s.split(' ');
  const result = new Array(words.length).fill('');

  for (const word of words) {
    const order = parseInt(word.slice(-1));
    const actualWord = word.substring(0, word.length - 1);

    result[order - 1] = actualWord;
  }

  return result.join(' ');
}
