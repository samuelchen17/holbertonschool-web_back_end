const createInt8TypedArray = (length, position, value) => {
  // create buffer
  const buffer = new ArrayBuffer(length);
  // Create an Int8Array view of the buffer
  const view = new Int8Array(buffer);

  if (position >= length || position < 0) {
    throw new Error('Position outside range');
  }
  view[position] = value;

  return buffer;
};

export default createInt8TypedArray;
