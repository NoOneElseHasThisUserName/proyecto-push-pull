// Similar a args en Python

function sumaConArgumentos() {
  let suma = 0;
  for (let i = 0; i < arguments.length; i++) {
    suma += arguments[i];
  }
  return suma;
}

const resultado = sumaConArgumentos(5, 10, 15, 20);
console.log(`La suma es: ${resultado}`);
