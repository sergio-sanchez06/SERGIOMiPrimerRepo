const mostrar = document.getElementById("mostrar");

mostrar.onclick = function () {

    const salida = document.getElementById("salida");

    var nombre = document.getElementById("nombre").value;
    var edad = parseInt(document.getElementById("edad").value);
    var hermanos = parseInt(document.getElementById("hermanos").value);
    var cadena = "15";

    var salida_mostrar = "";

    console.log(`Dentro de 15 años tu edad será ${edad + 15}`);
    salida_mostrar += `Dentro de 15 años tu edad será ${edad + 15} <br>` 
    salida_mostrar += `Dentro de 15 años tu edad será ` + edad + cadena + "<br>";
    console.log(`Dentro de 15 años tu edad será ` + edad + cadena)+ "<br>";

    salida_mostrar += typeof (edad) + "<br>";
    salida_mostrar += typeof (nombre) + "<br>";

    salida_mostrar += `La cadena 15 pasada a entero` + parseInt(cadena) + "<br>";
    salida_mostrar += `La cadena 15 pasada a float` + parseFloat(cadena);

    salida.innerHTML = salida_mostrar;

}