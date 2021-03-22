#!/usr/bin/node
if (process.argv[2] && Number(process.argv[2])) {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
