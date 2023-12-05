/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function (fn, t) {
  return async function (...args) {
    return new Promise(async (resolve, reject) => {
      let id = setTimeout(() => {
        reject("Time Limit Exceeded");
      }, t);
      let res;
      try {
        res = await fn(...args);
      } catch (error) {
        reject(error);
      }
      clearInterval(id);
      resolve(res);
    });
  };
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */
