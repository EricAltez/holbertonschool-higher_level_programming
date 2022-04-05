#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const numb = [];
  const len = process.argv.length;
  let i = 2;
  let second = 0;
  let mayor = 0;
  while (i < len) {
    numb.push(parseInt(process.argv[i]));
    i++;
  }
  i = 0;
  numb.sort();
  while (i < len - 2) {
    if (numb[i] > mayor) {
      second = mayor;
      mayor = numb[i];
    }
    i++;
  }
  console.log(second);
}
