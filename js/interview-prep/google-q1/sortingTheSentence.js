/**
 * @param {string} s
 * @return {string}
 */
const sortSentence = function (s) {
  // grab all the strings and split them by whitespace
  // map over each item and sort them by the last character (which should be the number)
  const chars = s.split(' ').map(word => ({
    word: word.substring(0, word.length - 1),
    order: parseInt(word[word.length - 1])
  }));

  chars.sort((a, b) => a.order - b.order);

  return chars.map(({ word }) => word).join(' ');
};