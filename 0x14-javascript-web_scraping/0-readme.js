#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 3) {
    console.error('Usage: ./0-readme.js <file_path>');
    process.exit(1);
}

const filePath = process.argv[2];

try {
    const fileContent = fs.readFileSync(filePath, 'utf8');
    console.log(fileContent);
} catch (error) {
    console.error(error);
}
