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

        // Realizamos un bucle entre 2 y el numero anterior al introducido por parametro 
        // para ver si existe algun numero por el cual sea divisible 
        // Usaremos un bucle do while ya que no sabemos el numero de iteraciones que realizará el bucle
        // Esto se debe a que el numero de iteraciones puede ser inferior al numero que delimina el final del rango a buscar

        var i = 2;

        do{

            //Si lo encontramos almacenamos en primo el valor false, lo que provoca la finalización del bucle
            if (numero % i === 0) {

                primo = false;

            }

            i++;

        }while(primo && i < numero);

        if (primo) {

            console.log(`${numero} es primo`);
            resultado.innerHTML = `${numero} es primo`;

        } else {

            console.log(`${numero} es primo`);
            resultado.innerHTML = `${numero} no es primo`;

        }


    }

}