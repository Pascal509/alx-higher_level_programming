#!/usr/bin/node

// const request = require('request');

// const ID = '18';
// const url = process.argv[2];

// // Function to count how many times Wedge Antilles appears in the film list
// function countFilms (films) {
//   let count = 0;
//   films.forEach(film => {
//     if (film.characters.includes(`${url}people/${ID}/`)) {
//       count++;
//     }
//   });
//   return count;
// }

// // Send a request to the provided API URL
// request(url, (error, response, body) => {
//   if (error) {
//     console.error('Error:', error);
//     return;
//   }

//   try {
//     const data = JSON.parse(body);
//     if (data && data.results) {
//       // Count the films with Wedge Antilles
//       const wedgeCount = countFilms(data.results);
//       console.log(wedgeCount);
//     } else {
//       console.log('No results found');
//     }
//   } catch (e) {
//     console.error('Failed to parse JSON:', e);
//   }
// });

// Prints the number of moviesthe character is present
const request = require('request');
let number = 0;

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          number += 1;
        }
      });
    });
    console.log(number);
  }
});
