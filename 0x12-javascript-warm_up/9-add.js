#!/usr/bin/node
function add(a, b) {
  return a + b;
}
if (process.argv.length !== 4) {
  console.log('Usage: scriptName.js <first_integer> <second_integer>');
} else {
  const num1 = parseInt(process.argv[2]);
  const num2 = parseInt(process.argv[3]);
  if (!isNaN(num1) && !isNaN(num2)) {
    const result = add(num1, num2);
    console.log('The addition of', num1, 'and', num2, 'is:', result);
  } else {
    console.log('Invalid input. Please provide two valid integers.');
  }
}
