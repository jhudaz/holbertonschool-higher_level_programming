#!/usr/bin/node
exports.esrever = function (list) {
  const data = [];
  for (let i = list.length - 1; i >= 0; i--) {
    data.push(list[i]);
  }
  return data;
};
