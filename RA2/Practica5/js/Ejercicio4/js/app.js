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

            listaPares += `<li>${i}</li>`;

        } else {

            listaPares += `<li>${i}</li>`;

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

    const numeroSumas = parseInt(document.getElementById("acumular"));

    var resultado = `La acumulacion de ${numeroSumas} es: `;

    var i = 1;

    do{

        ++i;

    }while(i <= numeroSumas);

    resultado += i;

    acumulador.innerHTML = resultado;

}