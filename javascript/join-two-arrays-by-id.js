/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function (arr1, arr2) {
  let arr = arr1.concat(arr2);
  let obj = {};

  for (let val of arr) {
    let id = val.id;

    if (!obj[id]) {
      obj[id] = val;
    } else {
      let temp = obj[id];
      obj[id] = { ...temp, ...val };
    }
  }

  return Object.values(obj).sort((a, b) => a.id - b.id);
};
