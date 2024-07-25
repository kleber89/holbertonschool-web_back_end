export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  // Crear un nuevo ArrayBuffer de longitud 'length'
  const buffer = new ArrayBuffer(length);
  // Crear un DataView para manejar el ArrayBuffer
  const dataView = new DataView(buffer);
  // Establecer el valor Int8 en la posición especificada
  dataView.setInt8(position, value);
  // Retornar el DataView que contiene el ArrayBuffer actualizado
  return dataView;
}
