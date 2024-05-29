#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];

request.get('https://swapi-api.alx-tools.com/api/films/' + movieID, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
