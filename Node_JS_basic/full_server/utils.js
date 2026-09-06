import fs from 'fs';

const readDatabase = (filePath) =>
  new Promise((resolve, reject) => {
    if (!filePath) {
      reject(new Error('Cannot load the database'));
      return;
    }

    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');

      const fields = {};

      if (lines.length <= 1) {
        resolve(fields);
        return;
      }

      const students = lines.slice(1);

      for (const student of students) {
        const studentData = student.split(',');
        const firstName = studentData[0];
        const field = studentData[3];

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      }

      resolve(fields);
    });
  });

export default readDatabase;
