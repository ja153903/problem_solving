/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
const findTheDifference = function (s, t) {
  if (s.length === 0) {
    return t;
  }

  const mp = new Map();

  for (let i = 0; i < s.length; i++) {
    mp.set(s[i], (mp.get(s[i]) ?? 0) + 1);
  }

  for (let i = 0; i < t.length; i++) {
    if (!mp.has(t[i])) {
      return t[i];
    }

    const currentValue = mp.get(t[i]);

    if (currentValue - 1 < 0) {
      return t[i];
    }

    mp.set(t[i], currentValue - 1);
  }

  for (const [key, value] of mp.entries()) {
    if (value > 0) {
      return key;
    }
  }

  return "";
};
