// app.js - Adaptado 100% a tu HTML con IDs: screenVotacion, screenResultado, candidatos, resultados, btnRepetir

let votoActual = 0;

document.addEventListener("DOMContentLoaded", iniciarVotacion);

function iniciarVotacion() {
  const candidatos = clase.filter(alumno => alumno.esCandidato);
  if (candidatos.length !== 3) {
    alert("Error: deben haber exactamente 3 candidatos con esCandidato = true");
    return;
  }
  siguienteVotante();
}

function siguienteVotante() {
  if (votoActual >= clase.length) {
    mostrarResultados();
    return;
  }

  const votante = clase[votoActual];

  // Si ya votó (en caso de repetición), pasamos al siguiente
  if (votante.haVotado) {
    votoActual++;
    siguienteVotante();
    return;
  }

  // Mostrar nombre del votante
  document.getElementById("nombreVotante").textContent = votante.nombre;

  // Limpiar y generar candidatos
  const container = document.getElementById("candidatos");
  container.innerHTML = "";

  clase
    .filter(a => a.esCandidato)
    .forEach(candidato => {
      const div = document.createElement("div");
      div.className = "candidato";
      div.textContent = candidato.nombre;
      div.dataset.id = candidato.id;

      div.onclick = function () {
        document.querySelectorAll(".candidato")
          .forEach(el => el.classList.remove("seleccionado"));
        this.classList.add("seleccionado");
      };

      container.appendChild(div);
    });

  // Evento del botón votar
  document.getElementById("btnVotar").onclick = function () {
    const seleccionado = document.querySelector(".candidato.seleccionado");
    if (!seleccionado) {
      alert("Por favor, selecciona un candidato antes de votar.");
      return;
    }

    const idCandidato = parseInt(seleccionado.dataset.id);
    const candidatoElegido = clase.find(a => a.id === idCandidato);

    if (votante.votar(candidatoElegido)) {
      votoActual++;
      siguienteVotante();
    } else {
      alert("Voto no válido. Inténtalo de nuevo.");
    }
  };
}

// Contar votos
function contarVotos() {
  const votos = {};
  clase.filter(a => a.esCandidato).forEach(c => votos[c.id] = 0);

  clase.forEach(alumno => {
    if (alumno.haVotado && alumno.votoEmitidoA) {
      votos[alumno.votoEmitidoA.id]++;
    }
  });
  return votos;
}

// Mostrar resultados finales
function mostrarResultados() {
  document.getElementById("screenVotacion").classList.add("oculto");
  document.getElementById("screenResultado").classList.remove("oculto");

  const divResultados = document.getElementById("resultados");
  const votos = contarVotos();

  const ranking = clase
    .filter(a => a.esCandidato)
    .map(c => ({ alumno: c, votos: votos[c.id] }))
    .sort((a, b) => b.votos - a.votos);

  let html = "<h3>Resultados de la votación:</h3>";
  ranking.forEach(p => {
    html += `<p><strong>${p.alumno.nombre}</strong>: ${p.votos} voto(s)</p>`;
  });
  divResultados.innerHTML = html;

  const primero = ranking[0];
  const segundo = ranking[1];
  const tercero = ranking[2];

  const empateDelegado = ranking.filter(p => p.votos === primero.votos).length > 1;
  const empateSubdelegado = !empateDelegado && tercero && segundo.votos === tercero.votos;

  if (empateDelegado || empateSubdelegado) {
    const tipo = empateDelegado ? "DELEGADO/A" : "SUBDELEGADO/A";
    const nombres = empateDelegado
      ? ranking.filter(p => p.votos === primero.votos).map(p => p.alumno.nombre).join(" y ")
      : `${segundo.alumno.nombre} y ${tercero.alumno.nombre}`;

    divResultados.innerHTML += `
      <p class="ganador empate">
        ¡EMPATE EN ${tipo} entre ${nombres}!<br>
        Se repetirá la votación completa.
      </p>
    `;
    document.getElementById("btnRepetir").classList.remove("oculto");
  } else {
    divResultados.innerHTML += `
      <p class="ganador">DELEGADO/A: ${primero.alumno.nombre} (${primero.votos} votos)</p>
      <p class="ganador">SUBDELEGADO/A: ${segundo.alumno.nombre} (${segundo.votos} votos)</p>
    `;
  }
}

// Botón para repetir votación en caso de empate
document.getElementById("btnRepetir").onclick = function () {
  clase.forEach(alumno => {
    alumno.haVotado = false;
    alumno.votoEmitidoA = null;
  });

  votoActual = 0;

  document.getElementById("screenResultado").classList.add("oculto");
  document.getElementById("screenVotacion").classList.remove("oculto");
  document.getElementById("btnRepetir").classList.add("oculto");
  document.getElementById("resultados").innerHTML = "";

  siguienteVotante();
};