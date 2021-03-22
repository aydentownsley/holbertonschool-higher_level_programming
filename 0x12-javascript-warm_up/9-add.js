#!/usr/bin/node
function add (a, b) {
  return a + b;
}

if ((process.argv[2] && Number(process.argv[2])) &&
  (process.argv[3] && Number(process.argv[3]))) {
  console.log(add(Number(process.argv[2]), Number(process.argv[3])));
} else {
  console.log('NaN');
}
