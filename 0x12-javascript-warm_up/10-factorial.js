#!/usr/bin/node
function factorial(n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
if (process.argv.length !== 3) {
  console.log('Usage: scriptName.js <integer>');
} else {
  const num = parseInt(process.argv[2]);
  if (!isNaN(num)) {
    const result = factorial(num);
    console.log('The factorial of', num, 'is:', result);
  } else {
    console.log('Invalid input. Please provide a valid integer.');
  }
}
