export default function updateUniqueItems(map) {
  // Verificar si el argumento es una instancia de Map
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  // Iterar sobre los elementos del mapa
  map.forEach((quantity, item) => {
    // Si la cantidad es 1, actualizar la cantidad a 100
    if (quantity === 1) {
      map.set(item, 100);
    }
  });

  // Retornar el mapa actualizado
  return map;
}
