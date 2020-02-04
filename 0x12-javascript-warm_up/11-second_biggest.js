#!/usr/bin/node
const data = process.argv;
if (data.length > 3) {
  const numbers1 = [];
  for (let i = 2; i < data.length; i++) {
    numbers1.push(Number(data[i]));
  }
  let maxVal = Math.max(...numbers1);
  const numbers2 = [];
  for (let i = 0; i < numbers1.length; i++) {
    if (numbers1[i] !== maxVal) {
      numbers2.push(numbers1[i]);
    }
  }
  maxVal = Math.max(...numbers2);
  console.log(maxVal);
} else {
  console.log(0);
}
