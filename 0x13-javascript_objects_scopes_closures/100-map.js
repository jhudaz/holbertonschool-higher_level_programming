#!/usr/bin/node
const list = require("./100-data");
const newList = list.list.map((value, index) => value * index)
console.log(list.list);
console.log(newList);
