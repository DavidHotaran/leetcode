/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
  if (n === 0) {
    return arr.slice();
  }
  let temp = [];

  for (let i = 0; i <= arr.length - 1; i++) {
    if (Array.isArray(arr[i])) {
      let newArr = flat(arr[i], n - 1);
      temp.push(...newArr);
    } else {
      temp.push(arr[i]);
    }
  }

  return temp;
};
