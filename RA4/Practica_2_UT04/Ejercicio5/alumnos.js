// alumnos.js - VERSIÓN 100% FUNCIONAL (los votos SÍ se cuentan)

class Alumno {
  static numAlumnos = 0;

  constructor(nombre, esCandidato = false) {
    Alumno.numAlumnos++;
    this.id = Alumno.numAlumnos;
    this.nombre = nombre;
    this.esCandidato = esCandidato;
    this.haVotado = false;
    this.votoEmitidoA = null;  // ¡¡ESTO ES CLAVE!!
  }

  votar(candidato) {
    if (!candidato.esCandidato) {
      console.warn("Solo se puede votar a candidatos");
      return false;
    }
    if (this.haVotado) {
      console.warn(this.nombre + " ya votó");
      return false;
    }

    this.haVotado = true;
    this.votoEmitidoA = candidato;  // ¡¡AQUÍ SE GUARDA EL VOTO!!
    return true;
  }
}

// === CREACIÓN DE LA CLASE (12 alumnos) ===
const clase = [
  new Alumno("Ana López García", true),
  new Alumno("Carlos Martínez Ruiz", true),
  new Alumno("Lucía Fernández Pérez", true),
  new Alumno("Pablo Sánchez Torres"),
  new Alumno("María González Díaz"),
  new Alumno("Diego Romero Vega"),
  new Alumno("Sofía Herrera Molina"),
  new Alumno("Alejandro Castro Jiménez"),
  new Alumno("Elena Navarro Ortiz"),
  new Alumno("Javier Morales Cano"),
  new Alumno("Carmen Ruiz Serrano"),
  new Alumno("Rubén Domínguez Gil")
];

// Para que funcione con <script src="alumnos.js"></script>
window.clase = clase;