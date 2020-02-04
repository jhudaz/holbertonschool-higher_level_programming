#!/usr/bin/node
exports.addMeMaybe = function (n, action) {
  let value = 1;
  for (let i = 0; i < n; i++) {
    value++;
  }
  return action(value);
};
