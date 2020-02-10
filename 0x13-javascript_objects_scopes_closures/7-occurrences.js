#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return (list.reduce((i, value) => i + (value === searchElement), 0));
};
