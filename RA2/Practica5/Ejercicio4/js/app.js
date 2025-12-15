const CALCULAR_TABLA = function () {

    const tabla = document.getElementById("tabla");

    var numero = parseInt(document.getElementById("num_multiplicar").value);

    var tablaMultiplicar = `<h2>Tabla de multiplicar del ${numero}</h2>`;
    tablaMultiplicar += `<table>`;
    tablaMultiplicar += `<tr>
                                <th> Multiplicacion</th>
                                <th>Resultado</th>
                            </tr>`;

    for (let i = 1; i <= 12; i++) {

        tablaMultiplicar += `<tr><td>${numero} * ${i}</td> <td>${numero * i}</td></tr>`;
    }

    tablaMultiplicar += `</table>`;
    tabla.innerHTML = tablaMultiplicar;

}

const CALCULAR_PARES_IMPARES = function(){

    const pares = document.getElementById("par");
    const impares = document.getElementById("impar");

    var inicio = parseInt(document.getElementById("inicio").value);
    var fin = parseInt(document.getElementById("fin").value);

    var listaPares = `<h2>Lista de los numeros pares</h2>`;
    listaPares += `<ul>`;

    var listaImpares = `<h2>Lista de los numeros impares</h2>`;
    listaImpares += `<ul>`;

    var i = inicio

    while (i <= fin) {

        if (i % 2 == 0) {

            //Si el resto de dividir i entre 2 es 0, insertamos el numero en la lista de los pares
            listaPares += `<li>${i}</li>`; 

        } else {

            //Si el resto de dividir i entre 2 es 0, insertamos el numero en la lista de los impares
            listaImpares += `<li>${i}</li>`; 
        }

        i++;

    }

    listaPares += `</ul>`;
    listaImpares += `</ul>`;
    
    pares.innerHTML = listaPares;
    impares.innerHTML = listaImpares;


}

const ACUMULADOR = function(){

    const acumulador = document.getElementById("acumulador");
    const numeroSumas = parseInt(document.getElementById("acumular").value);
    const MOSTRARCONSOLA = document.getElementById("mostrarConsola").checked;

    if(isNaN(numeroSumas) || numeroSumas < 1){

        acumulador.innerHTML = "Introduce un numero mayor o igual a 1";
        return;

    }

    var total = 0;

    var i = 1;

    var pasos = "";

    do{

        total += i;

        /* De esta manera creaamos la secuencia de suma. Si i === i imprime i, 
        sino imprime el signo + mas el valor de i*/

        pasos += (i === 1) ? `${i}` : ` + ${i}`; 

        i++;

    }while(i <= numeroSumas);

    const RESULTADO = `La acumulacion de los primero ${numeroSumas} numeros es: ${total}`;
    acumulador.innerHTML = RESULTADO;

    if(MOSTRARCONSOLA){

        console.log("Paso a paso de la acumulación: ", pasos);
        console.log("Total acumulado: ", total);

        let pre = 5;
        let post = 10;

        /*Diferencia de preincremento y postincremento
        El pre incremento primero realiza la suma del valor de la variable mas 1 y despues almacena y muestra el nuevo valor en la variable
        El post incremento primero almacena o devuelve el valor actual de la variable y despues realiza la suma.*/

        console.log("Preincremento (++pre): ", ++pre);
        console.log("Postincremento (post++): ", post++);
        console.log("Valor final de pre: ", pre);
        console.log("Valor final de post:", post);

    }

}