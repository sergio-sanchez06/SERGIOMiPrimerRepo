function calcular() {
        
    var resultado = "";
    var num1, num2;
    var valido = false;

        do {

          num1 = parseInt(prompt("Introduce el primer numero: "));
          num2 = parseInt(prompt("Introduce el segundo numero: "));

          if (!isNaN(num1) && !isNaN(num2)) {
            valido = true;
          }else{

            alert("Entrada no valida. Debes introducir dos números");

          }
          
        } while (!valido);

        

        var suma = num1;
        suma += num2;
        var resta = num1 - num2;
        var producto = num1;
        producto *= num2;
        var cociente = num1 / num2;
        var modulo = num1 % num2;

        resultado += `<p>Suma (${num1} += ${num2}): ${suma}</p>`;
        resultado += `<p>Suma (${num1} - ${num2}): ${resta}</p>`;
        resultado += `<p>Producto (${num1} *= ${num2}): ${producto}</p>`;
        resultado += `<p>Cociente (${num1} / ${num2}): ${cociente}</p>`;
        resultado += `<p>Modulo (${num1} % ${num2}): ${modulo}</p>`;

        // Comparaciones entre los numeros

        resultado += `<p>Igualdad (${num1} == ${num2}): ${
          num1 == num2 ? "true" : "false"
        }</p>`;
        resultado += `<p>Identidad (${num1} === ${num2}): ${
          num1 === num2 ? "true" : "false"
        }</p>`;
        resultado += `<p>Diferencia (${num1} != ${num2}): ${
          num1 != num2 ? "true" : "false"
        }</p>`;
        resultado += `<p>Mayor que (${num1} > ${num2}): ${
          num1 > num2 ? "true" : "false"
        }</p>`;
        resultado += `<p>Menor o igual (${num1} <= ${num2}): ${
          num1 <= num2 ? "true" : "false"
        }</p>`;

        // Diferencia entre == ===

        resultado += `<p>El operador == evalua si ambos operandos son iguales aplicando una conversion de tipos <br>
            El operador === evalua si ambos operandos tienen el mismo valor y son del mismo tipo</p>`;

        // Operadores logicos

        if (num1 > 0 && num2 > 0) {

          resultado += `<p>Ambos operadores son positivos</p>`;

        } else {
          resultado += `<p>Uno o ninguno de los operadores es positivo</p>`;
          
        }

        if (num1 > 10 || num2 > 10) {

          resultado += `<p>Al menos uno de los valores es mayor que 10.</p>`;

        } else {

          resultado += `<p>Ninguno de los valores es mayor que 10.</p>`;

        }

        // Operador ternario

        const MAYORQUECIEN = suma > 100 ? "mayor" : "menor";

        resultado += `El resultado de la suma es ${MAYORQUECIEN} que 100`;

        document.getElementById("resultado").innerHTML = resultado;

      }