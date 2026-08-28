const cleanSet = (set, startString) => {
  let string = '';

  if (!startString) {
    return '';
  }

  set.forEach((element) => {
    if (element.startsWith(startString)) {
      const value = element.slice(startString.length);

      if (string === '') {
        string += value;
      } else {
        string += `-${value}`;
      }
    }
  });

  return string;
};

export default cleanSet;
