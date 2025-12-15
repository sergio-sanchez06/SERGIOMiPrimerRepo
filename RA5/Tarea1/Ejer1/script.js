document.addEventListener("DOMContentLoaded", (e) => {

    const form = document.getElementById("form");

    form.addEventListener("submit", (envio) => {

        envio.preventDefault()

        const select = document.getElementById("selectEquipos").value
        const input = document.getElementById("input").value.trim()

        document.getElementById("pInput").innerHTML = `El equipo seleccionado mediante el Input es: ${input}`;
        document.getElementById("pSelect").innerHTML = `El equipo seleccionado mediante el Input es: ${select}`;

    })

})