document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("form");
  const equipo = document.getElementById("equipos");

  const jugadores = document
    .getElementById("jugadores");

  function updateTeam() {

    const seleccionado = equipo.value;
    const plantillas = jugadores.querySelectorAll("optgroup")

    plantillas.forEach((plantilla) => {
      if (plantilla.id === seleccionado) {
        plantilla.disabled = false;
        jugadores.value = plantilla.querySelector("option").value
      } else {
        plantilla.disabled = true;
      }
    });
  }

  equipo.addEventListener("change", updateTeam);

  updateTeam()

});
