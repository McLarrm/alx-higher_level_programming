#!/usr/bin/node
const executionUtils = {
  executeXTimes: function(x, theFunction) {
    for (let i = 0; i < x; i++) {
      theFunction();
    }
  }
};
module.exports = executionUtils;
