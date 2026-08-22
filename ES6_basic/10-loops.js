export default function appendToEachArrayValue(array, appendString) {
  for (var value of array) {
    value = appendString + value;
  }

  return array;
}
