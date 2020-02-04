#!/usr/bin/node
exports.callMeMoby = function (n, action) {
  for (let i = 0; i < n; i++) {
    action();
  }
};
