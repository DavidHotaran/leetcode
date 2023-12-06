var TimeLimitedCache = function () {
  this.cache = new Map();
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
  if (this.cache.has(key)) {
    let obj = this.cache.get(key);
    if (obj.expired) {
      let timeout = setTimeout(
        () => (this.cache.get(key).expired = true),
        duration
      );
      this.cache.set(key, { value: value, expired: false, timeout: timeout });
      return false;
    } else {
      clearTimeout(this.cache.get(key).timeout);
      let timeout = setTimeout(
        () => (this.cache.get(key).expired = true),
        duration
      );
      this.cache.set(key, { value: value, expired: false, timeout: timeout });
      return true;
    }
  } else {
    let timeout = setTimeout(
      () => (this.cache.get(key).expired = true),
      duration
    );
    this.cache.set(key, { value: value, expired: false, timeout: timeout });
    return false;
  }
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
  if (this.cache.has(key)) {
    if (this.cache.get(key).expired) {
      return -1;
    } else {
      return this.cache.get(key).value;
    }
  } else {
    return -1;
  }
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
  let count = 0;
  for (const [_, value] of this.cache) {
    if (!value.expired) {
      count += 1;
    }
  }
  return count;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
