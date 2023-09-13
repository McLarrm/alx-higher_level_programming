#!/usr/bin/node

const fs = require('fs');
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];
fs.readFile(sourceFile1, 'utf8', (err1, data1) => {
  if (err1) {
    console.error(err1);
    return;
  }
  fs.readFile(sourceFile2, 'utf8', (err2, data2) => {
    if (err2) {
      console.error(err2);
      return;
    }
    const concatenatedData = data1 + data2;
    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err3) => {
      if (err3) {
        console.error(err3);
        return;
      }
      console.log(`Concatenated files ${sourceFile1} and ${sourceFile2} to ${destinationFile}`);
    });
  });
});
