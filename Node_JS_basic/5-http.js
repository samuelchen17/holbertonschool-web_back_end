const http = require('http');
const fs = require('fs');

const PORT = 1245;
const DB_FILE = process.argv[2];

function countStudents(path, body) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (error, fileContent) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = fileContent
        .split('\n')
        .filter((line) => line.trim() !== '');

      const students = lines.slice(1);
      const total = students.length;

      const fields = {};

      for (const student of students) {
        const studentData = student.split(',');
        const firstName = studentData[0];
        const field = studentData[3];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstName);
      }

      body.push(`Number of students: ${total}`);
      Object.keys(fields).forEach((field) => {
        body.push(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`,
        );
      });
      resolve(body.join('\n'));
    });
  });
}

const app = http.createServer(async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.statusCode = 200;

    const body = ['This is the list of our students'];

    try {
      const data = await countStudents(DB_FILE, body);
    } catch (err) {
      res.end(err.message);
    }

    res.end(data);
  } else {
    res.statusCode = 404;
    res.end('404 Not found');
  }
});

app.listen(PORT);

module.exports = app;
