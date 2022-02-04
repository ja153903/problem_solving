/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
const findAnagrams = function (s, p) {
  if (p.length > s.length) {
    return [];
  }

  // go through all substrings of len(p) within s
  // check if any of those are anagrams
  // add to result if anagram
  const result = [];
  const seen = new Set();
  const anagrams = new Set();

  const n = p.length;

  for (let i = 0; i <= s.length - n; i++) {
    const substr = s.substring(i, i + n);

    if (anagrams.has(substr)) {
      result.push(i);
    } else if (seen.has(substr)) {
      continue;
    } else if (isAnagram(p, substr)) {
      anagrams.add(substr);
      result.push(i);
    } else {
      seen.add(substr);
    }
  }

  return result;
};

/**
 * @param {string} s
 * @param {string} t
 * @returns {boolean}
 */
function isAnagram(s, t) {
  if (s.length !== t.length) {
    return false;
  }

  const counter = new Map();

  for (const ch of s.split("")) {
    counter.set(ch, (counter.get(ch) ?? 0) + 1);
  }

  for (const ch of t.split("")) {
    if (!counter.has(ch)) {
      return false;
    }

    if (counter.get(ch) - 1 < 0) {
      return false;
    }

    counter.set(ch, counter.get(ch) - 1);
  }

  return [...counter.values()].reduce((acc, val) => acc + val) === 0;
}

console.log(findAnagrams("cbaebabacd", "abc"));
console.log(findAnagrams("abab", "ab"));

/**
 * 
 * @param {string} s 
 * @param {string} t 
 * @returns {boolean}
 */
function slidingWindowSolution(s, t) {
  const result = [];
  
  if (t.length > s.length) {
    return result;
  }

  const counter = new Map(); 
  
  for (const ch of t.split("")) {
    counter.set(ch, (counter?.get(ch) ?? 0) + 1);
  }
  
  let begin = 0;
  let end = 0;

  let size = counter.size;
  
  while (end < s.length) {
    const ch = s[end];

    if (counter.has(ch)) {
      counter.set(ch, counter.get(ch) - 1);
      if (counter.get(ch) === 0) {
        size--;
      }
    }
    
    end++;
    
    while (size === 0) {
      const ch = s[begin];
      // This is how we make sure that we're only checking
      // for characters relevant to the anagram
      if (counter.has(ch)) {
        counter.set(ch, counter.get(ch) + 1);
        if (counter.get(ch) > 0) {
          size++;
        }
      }
      
      if (end - begin === t.length) {
        result.push(begin);
      }
      
      begin++;
    }
  }
  
  return result;
}

console.log(slidingWindowSolution("cbaebabacd", "abc"));
console.log(slidingWindowSolution("abab", "ab"));