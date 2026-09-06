import readDatabase from '../utils';

const DB_FILE = process.argv[2];

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const db = await readDatabase(DB_FILE);

      const fields = Object.keys(db).sort((a, b) =>
        a.toLowerCase().localeCompare(b.toLowerCase()),
      );

      const body = ['This is the list of our students'];

      fields.forEach((field) => {
        body.push(
          `Number of students in ${field}: ${database[field].length}. List: ${database[field].join(', ')}`,
        );
      });

      res.status(200).send(body.join('\n'));
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const database = await readDatabase(process.argv[2]);

      res.status(200).send(`List: ${database[major].join(', ')}`);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
ß;
