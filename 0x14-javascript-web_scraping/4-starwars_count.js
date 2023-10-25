#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18; // Character ID for Wedge Antilles

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const moviesWithWedge = filmData.results.filter((film) => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
    console.log(moviesWithWedge.length);
  } else {
    console.error(error || `Error: Unable to fetch movie information from ${apiUrl}`);
  }
});
