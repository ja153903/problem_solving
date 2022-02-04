/**
 * @param {string} s
 * @return {string}
 */
const minRemoveToMakeValid = function (s) {
  const stack = [];
  const idxStack = [];

  // go through each element in the string
  // if we see an open parens, then we should
  // add it to the list
  // if we see a closing parens, we should check out stack
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      idxStack.push(i);
      stack.push("*");
    } else if (s[i] === ")") {
      if (idxStack.length === 0) {
        stack.push("*");
      } else {
        const open = idxStack.pop();
        stack[open] = "(";
        stack.push(")");
      }
    } else {
      stack.push(s[i]);
    }
  }

  return stack.filter((char) => char !== "*").join("");
};

console.log(minRemoveToMakeValid("lee(t(c)o)de)"));
