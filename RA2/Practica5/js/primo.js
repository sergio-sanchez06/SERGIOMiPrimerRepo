    /*

    Escriba un script que analice el valor de una variable llamada número (que 
    contiene un número entero positivo mayor que 1) y nos indique si se trata de un 
    número primo o no. Utilice métodos de console para visualizar mensajes que 
    puedan ayudarte a seguir la ejecución del código

    */

const boton = document.getElementById("boton");

boton.onclick = function () {

    const resultado = document.getElementById("resultado");

    var numero = parseInt(document.getElementById("numero").value);

    if (numero <= 1) {

        console.log("El numero debe ser mayor a 1");

    } else {

        var primo = true;

        for (var i = 2; i < numero - 1; i++) {

            if (numero % i === 0) {

                primo = false;
                break;

            }

        }

        if (primo) {

            console.log(`${numero} es primo`);
            resultado.innerHTML = `${numero} es primo`;

        } else {

            console.log(`${numero} es primo`);
            resultado.innerHTML = `${numero} no es primo`;

        }


    }

}