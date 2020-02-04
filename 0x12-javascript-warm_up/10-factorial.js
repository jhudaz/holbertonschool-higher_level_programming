#!/usr/bin/node
const number = Number(Math.trunc(process.argv[2]));

function factorial (n) {
  if (!n) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(number));
