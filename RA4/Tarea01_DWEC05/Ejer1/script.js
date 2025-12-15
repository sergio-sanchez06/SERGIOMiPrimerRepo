document.addEventListener("DOMContentLoaded", (event) => {
  const form = document.getElementById("form");
  const equiposSelect = document.getElementById("equiposSelect");
  const equiposInput = document.getElementById("equiposInput");
  const resultadoSelect = document.getElementById("resultadoSelect");
  const resultadoInput = document.getElementById("resultadoInput");

  form.addEventListener("submit", (event) => {
    event.preventDefault();

    if (equiposInput.value === "" || equiposSelect.value === "") {
      alert("Debes introducir un equipo");
    } else {
      resultadoInput.textContent = `Equipo seleccionado en el input: ${equiposInput.value}`;
      resultadoSelect.textContent = `Equipo seleccionado en el select: ${equiposSelect.value}`;
    }
  });
});
