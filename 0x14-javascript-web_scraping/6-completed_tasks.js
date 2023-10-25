#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const todosData = JSON.parse(body);
    const completedTasks = {};

    for (const todo of todosData) {
      if (todo.completed) {
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId]++;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    }

    console.log(completedTasks);
  } else {
    console.error(error || `Error: Unable to fetch data from ${apiUrl}`);
  }
});
