#!/usr/bin/node
function factorial (a) {
  if (a > 0) {
    return factorial(a - 1) * a;
  } else {
    return 1;
  }
}

if (process.argv[2] && Number(process.argv[2])) {
  console.log(factorial(Number(process.argv[2])));
} else if (process.argv.length === 2) {
  console.log(1);
}
