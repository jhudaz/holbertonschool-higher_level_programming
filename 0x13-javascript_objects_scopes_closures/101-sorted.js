#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = Object.entries(dict);
const keys = [];
for (const data of newDict) keys.push(data[1]);

const uniques = [...new Set(keys)];
const values = [];

for (let i = 0; i < uniques.length; i++) {
  const list = [];
  for (const [index, value] of newDict) {
    if (value === uniques[i]) list.push(index);
  }
  values.push(list);
}

const dicti = {};
for (let i = 0; i < uniques.length; i++) {
  dicti[uniques[i]] = values[i];
}

console.log(dicti);
