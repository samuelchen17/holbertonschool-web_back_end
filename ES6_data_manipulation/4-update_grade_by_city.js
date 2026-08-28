const updateStudentGradeByCity = (students, city, newGrades) => {
  // filter to get students from the city
  // go through each one using map
  // find the matching id from newGrades
  // conditional statement to see if new grade exists, if yes update the grade, else N/A
  // return the filtered students with new grade updated
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const studentGrade = newGrades.find(
        (grade) => grade.studentId === student.id,
      );

      const updatedGrade = studentGrade ? studentGrade.grade : 'N/A';

      return { ...student, grade: updatedGrade };
    });
};

export default updateStudentGradeByCity;
