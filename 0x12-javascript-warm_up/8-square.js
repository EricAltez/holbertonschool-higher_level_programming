#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let i = 0;
  let c = 0;
  while (i < process.argv[2] && process.argv[2] > 0) {
    c = 'X'.repeat(process.argv[2]);
    console.log(c);
    i++;
  }
}
