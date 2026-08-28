const hasValuesFromArray = (arr, set) => {
  if (!Array.isArray(arr)) {
    return false;
  }

  return arr.every((value) => set.has(value));
};

export default hasValuesFromArray;
