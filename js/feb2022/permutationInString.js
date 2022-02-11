/**
 * This problem wants us to check if a permutation of s1 is in s2
 * we can do this via a sliding window algorithm
 *
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
function checkInclusion(s1, s2) {
  if (s1.length > s2.length) {
    return false;
  }

  const counter = new Map();

  for (const ch of s1.split("")) {
    counter.set(ch, (counter.get(ch) ?? 0) + 1);
  }

  let begin = 0;
  let end = 0;

  let size = counter.size;

  while (end < s2.length) {
    const ch = s2[end];

    if (counter.has(ch)) {
      counter.set(ch, counter.get(ch) - 1);
      if (counter.get(ch) === 0) {
        size--;
      }
    }

    end++;

    while (size === 0) {
      const ch = s2[begin];

      if (counter.has(ch)) {
        counter.set(ch, counter.get(ch) + 1);
        if (counter.get(ch) > 0) {
          size++;
        }
      }

      if (end - begin === s1.length) {
        return true;
      }

      begin++;
    }
  }

  return false;
}
