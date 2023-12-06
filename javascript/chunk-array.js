/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function (arr, size) {
  let ret = [];
  let i = 0;
  len = arr.length - 1;

  while (i <= len) {
    let temp = [];
    for (let j = 0; j < size; j++) {
      if (i <= len) {
        temp.push(arr[i]);
        i++;
      }
    }
    ret.push(temp);
  }

  return ret;
};
