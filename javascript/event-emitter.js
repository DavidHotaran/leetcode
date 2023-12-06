class EventEmitter {
  constructor() {
    this.events = {};
  }

  /**
   * @param {string} eventName
   * @param {Function} callback
   * @return {Object}
   */
  subscribe(eventName, callback) {
    let id = this.events[eventName];

    if (!id) {
      this.events[eventName] = [callback];
    } else {
      this.events[eventName].push(callback);
    }

    return {
      unsubscribe: () => {
        const index = this.events[eventName].indexOf(callback);
        if (index !== -1) {
          this.events[eventName].splice(index, 1);
        }
      },
    };
  }

  /**
   * @param {string} eventName
   * @param {Array} args
   * @return {Array}
   */
  emit(eventName, args = []) {
    let cbs = this.events[eventName];

    if (!cbs) {
      return [];
    }

    let ret = [];
    for (let cb of cbs) {
      ret.push(cb(...args));
    }
    return ret;
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
