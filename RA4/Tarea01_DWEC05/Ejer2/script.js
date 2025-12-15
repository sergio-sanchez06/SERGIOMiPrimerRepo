document.addEventListener("DOMContentLoaded", function () {
  let equipoSelect = document.getElementById("equipos");
  let jugadorSelect = document.getElementById("jugadores");

  function actualizarGrupos() {
    let seleccionado = equipoSelect.value;
    let grupos = jugadorSelect.querySelectorAll("optgroup");

    grupos.forEach(function (grupo) {
      if (grupo.id === seleccionado) {
        grupo.disabled = false;
        jugadorSelect.value = grupo.querySelector("option").value;
      } else {
        grupo.disabled = true;
      }
    });
  }

  equipoSelect.addEventListener("change", actualizarGrupos);

  actualizarGrupos();
});
