#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;

  characterUrls.forEach((url, index) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);

      // This ensures the characters print in the same order as in the list by waiting
      // until all previous character requests have completed before exiting.
      if (index === characterUrls.length - 1) {
        process.exit();
      }
    });
  });
});
