/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
  let cache = new Map();

  return function (...args) {
    const key = JSON.stringify(args.join(","));
    if (cache.has(key)) {
      return cache.get(key);
    } else {
      const val = fn(...args);
      cache.set(key, val);
      return val;
    }
  };
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */
