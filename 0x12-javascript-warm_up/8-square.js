#!/usr/bin/node
if (process.argv[2] && Number(process.argv[2])) {
  const size = process.argv[2];
  let line = '';
  for (let x = 0; x < size; x++) {
    for (let y = 0; y < size; y++) {
      line = line.concat('X');
    }
    console.log(line);
    line = '';
  }
} else {
  console.log('Missing size');
}
