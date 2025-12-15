const mostrar = document.getElementById("mostrar");

mostrar.onclick = function () {

    const salida = document.getElementById("salida");

    var nombre = document.getElementById("nombre").value;
    var edad = parseInt(document.getElementById("edad").value);
    var hermanos = parseInt(document.getElementById("hermanos").value);
    var cadena = "15"; //Cadena que parece un numero

    var salida_mostrar = "";

    salida_mostrar += `<p>Dentro de 15 años tu edad será ${edad + 15} </p>`
    
    //En este caso se mostrar la edad del usuario seguido de la cadena 15, esto se debe a que cadena almacena un string
    salida_mostrar += `<p>Dentro de 15 años tu edad será ` + edad + cadena + "</p>";

    //Mostramos los tipos de datos de las variables
    salida_mostrar += `<p>Tipo de dato de la variable edad ` + typeof (edad) + "</p>";
    salida_mostrar += `<p>Tipo de dato de la variable nombre ` + typeof (nombre) + "</p>";
    salida_mostrar += `<p>Tipo de dato de la variable hermanos ` + typeof (hermanos) + "</p>";
    salida_mostrar += `<p>Tipo de dato de la variable cadena ` + typeof (cadena) + "</p>";

    salida_mostrar += `<p>La cadena 15 pasada a entero: ` + parseInt(cadena) + "</p>";
    salida_mostrar += `<p>La cadena 15 pasada a float: ` + parseFloat(cadena);

    salida.innerHTML = salida_mostrar;

}