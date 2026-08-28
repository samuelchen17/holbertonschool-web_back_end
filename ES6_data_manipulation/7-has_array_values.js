const hasValuesFromArray = (arr, set) => {
  return arr.every((value) => set.has(value));
};

export default hasValuesFromArray;
