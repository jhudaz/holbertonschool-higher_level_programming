#!/usr/bin/node
let i = 1;
exports.logMe = function (item) {
  console.log(`${i}: ${item}`);
  i++;
};
