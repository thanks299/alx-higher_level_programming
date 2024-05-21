#!/usr/bin/node
const request = require('request');

const apiURL = 'https://swapi-api.alx-tools.com/api/films/'

request.get(apiURL, async (error, response, body) => {
    if (error) {
        console.error(error);
    } else {
        const movies = JSON.parse(body);
        let wedgeMovies = 0;
        for (const movie of movies.results) {
            for (const characterURL of movie.characters) {
                try {
                    const characterResponse = await new Promise((resolve, reject) => {
                        request.get(characterURL, (error, response, body) => {
                            if (error) {
                                reject(error);
                            } else {
                                resolve(body);
                            }
                        });
                    });
                    const character = JSON.parse(characterResponse);
                    if (character.name === 'Wedge Antilles') {
                        wedgeMovies++;
                    }
                } catch (error) {
                    console.error(error);
                }
            }
        }
        console.log(wedgeMovies);
    }
});
