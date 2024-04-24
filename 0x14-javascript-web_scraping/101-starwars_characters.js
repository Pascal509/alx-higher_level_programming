#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const movie = JSON.parse(body);
  const characters = movie.characters;
  let completedRequests = 0;

  // We will store character names to maintain the order
  const characterNames = new Array(characters.length);

  characters.forEach((url, index) => {
    request(url, function (error, response, body) {
      if (error) {
        console.error('Error:', error);
        return;
      }

      const character = JSON.parse(body);
      characterNames[index] = character.name;

      // Increment the completed requests counter
      completedRequests++;
      // Check if all requests are completed
      if (completedRequests === characters.length) {
        // All character requests completed, print names in order
        characterNames.forEach(name => console.log(name));
      }
    });
  });
});
