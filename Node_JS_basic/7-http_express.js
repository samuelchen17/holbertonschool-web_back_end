const express = require('express');

const app = express();
const PORT = 1245;
const DB_FILE = process.argv[2];
const countStudents = require('./3-read_file_async');

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students',async (req, res) => {
  const body = ['This is the list of our students'];

  try {
    const data = await countStudents(DB_FILE);
    body.push(data);
    res.end(body.join('\n'));
  } catch (err) {
    res.end(`${body.join('\n')}\n${err.message}`);
  }
});

app.listen(PORT);

module.exports = app;
