
/* Definimos una funcion para realizar los calculos de la tabla de multiplicar. En este caso usaremos un for
El bucle for se emplea cuando sabemos el numero de iteraciones que necesitamos realizar*/

function tablaMultiplicar(numero) {

    if(numero >= 0 && numero <= 10){

        const tabla = document.getElementById("tablaMultiplicar");
        let tablaMultiplicar = `<h2>Tabla de multiplicar del ${numero}</h2>`;
        tablaMultiplicar += `<table>`;
        tablaMultiplicar += `<tr>
                                <th> Multiplicacion</th>
                                <th>Resultado</th>
                                <th>Bucle</th>
                            </tr>`;

        for(let i = 0; i<=10;i++){

            tablaMultiplicar += `<tr><td>${numero} * ${i}</td> <td>${numero * i}</td><td>For</td></tr>`;
        }

        tablaMultiplicar += `</table>`;
        tabla.innerHTML = tablaMultiplicar;

    }else{

        alert('El numero introducido debe estar entre 0 y 10');
        document.getElementById("numero").value= '';

    }  

}

/* Definimos una funcion para realizar los calculos de la tabla de sumar. En este caso usaremos un while
El bucle while se emplea cuando no sabemos el número de iteraciones que necesitamos realizar. 
El contenido dentro del bucle solo se ejecutará si la condicion de entrada se cumple, 
por lo que puede ser que nunca llegue a ejecutarse*/

function tablaSuma(numero){

    if(numero >= 0 && numero <= 10){

        let tabla = document.getElementById('tablaSumar');
        let tablaSumar = `<h2>Tabla de Sumas del ${numero}</h2>`;
        tablaSumar += `<table>`;
        tablaSumar += `<tr>
                                <th>Suma</th>
                                <th>Resultado</th>
                                <th>Bucle</th>
                            <tr>`;

        let contador = 0;

        while(contador <=10){

            tablaSumar += `<tr><td>${numero} + ${contador}</td> <td>${numero + contador}</td><td>While</td></tr>`;
            contador++;
        }

        tablaSumar += `</table>`;
        tabla.innerHTML = tablaSumar;

    }else{

        alert('El numero introducido debe estar entre 0 y 10');
        document.getElementById("numero").value= '';

    } 

}

/* Definimos una funcion para realizar los calculos de la tabla de sumar. En este caso usaremos un while
El bucle do while tambien se emplea cuando no sabemos el número de iteraciones que necesitamos realizar. 
A diferencia del bucle while, el bucle do while ejecutará al menos una vez la logica de su interior.*/

function tablaDividir(numero){

    if(numero >= 0 && numero <= 10){

        let tabla = document.getElementById('tablaDividir');
        let tablaDividir = `<h2>Tabla de Dividir del ${numero}</h2>`;
        tablaDividir += `<table>`;
        tablaDividir += `<tr>
                                <th>Division</th>
                                <th>Resultado</th>
                                <th>Bucle</th>
                            </tr>`;

        let contador = numero;

        do{

            tablaDividir += `<tr><td>${contador} / ${numero}</td> <td>${contador / numero}</td><td>Do While</td></tr>`;
            contador+=numero;

        }while(contador <= numero * 10);

        tablaDividir += `</table>`;
        tabla.innerHTML = tablaDividir;

    }else{

        alert('El numero introducido debe estar entre 0 y 10');
        document.getElementById("numero").value= '';

    } 

}