#!/usr/bin/node

const fs = require('fs').promises;

async function readAndPrintFile() {
  try {
    const result = await fs.readFile(process.argv[2], 'utf-8');
    console.log(result);
  } catch (err) {
    console.log(err);
  }
}

readAndPrintFile();
