#!/usr/bin/node
const request = require('request');

const apiURL = process.argv[2];

request.get(apiURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movies = JSON.parse(body);
    const wedgeMovies = movies.results.filter(movie => {
      return movie.characters.includes('https://swapi-api.alx-tools.com/api/films/');
    });
    console.log(wedgeMovies.length);
  }
});
