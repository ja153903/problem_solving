/**
 * @param {string} s
 * @return {string}
 */
const removeDuplicates = function (s) {
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    if (!stack.length) {
      stack.push(s[i]);
    } else {
      if (stack[stack.length - 1] === s[i]) {
        stack.pop()
      } else {
        stack.push(s[i]);
      }
    }
  }
  
  return stack.join("");
};

console.log(removeDuplicates("abbaca"));