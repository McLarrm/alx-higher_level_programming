#!/usr/bin/node
const incrementUtils = {
  incrementAndCall: function(number, theFunction) {
    const incrementedNumber = number + 1;
    theFunction(incrementedNumber);
  }
};
module.exports = incrementUtils;
