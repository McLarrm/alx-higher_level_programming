#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    characterUrls.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (!charError && charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        } else {
          console.error(charError || `Error: Unable to fetch character data from ${characterUrl}`);
        }
      });
    });
  } else {
    console.error(error || `Error: Unable to fetch movie information from ${apiUrl}`);
  }
});
