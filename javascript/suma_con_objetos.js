/*
  Similar a kwargs en Python

  En JS se utiliza el operador de propagación "..."
*/

function sumaConObjetos(...numeros) {
  let suma = 0;
  for (const key in numeros) {
    suma += numeros[key];
  }
  return suma;
}

const numeros = { num1: 5, num2: 10, num3: 15, num4: 20 };
const resultado = sumaConObjetos(...Object.values(numeros));
console.log(`La suma es: ${resultado}`);