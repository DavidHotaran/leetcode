/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function (fn) {
  let ret = {};

  for (let i = 0; i <= this.length - 1; i++) {
    el = this[i];
    key = fn(el);
    if (!Object.hasOwn(ret, key)) {
      ret[key] = [el];
    } else {
      ret[key].push(el);
    }
  }

  return ret;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
