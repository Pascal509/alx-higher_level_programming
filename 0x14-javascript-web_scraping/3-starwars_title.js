#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const api = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(api, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  // Parse the JSON response body
  const data = JSON.parse(body);

  if (data && data.title) {
    console.log(data.title);
  } else {
    console.log('movie not found');
  }
});
