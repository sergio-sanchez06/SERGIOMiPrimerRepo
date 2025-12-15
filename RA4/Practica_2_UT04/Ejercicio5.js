class Alumno{

    constructor(nombre){

        this.nombre = nombre
        this.haVotado = false

    }

    votar(nombre){

        if(!this.haVotado){

            this.haVotado = true
            return nombre

        }else{

            return null

        }

    }

}

const clase = [
            new Alumno("Ana García"),
            new Alumno("Beto Pérez"),
            new Alumno("Carlos Ruiz"),
            new Alumno("Diana Soto"),
            new Alumno("Elena Torres"),
            new Alumno("Félix Vargas"),
            new Alumno("Gloria Vega"),
            new Alumno("Héctor Gil"),
            new Alumno("Irene López"),
            new Alumno("Javier Marín"),
            new Alumno("Laura Nieves"),
            new Alumno("Miguel Olmos"),
        ];

// Los 3 candidatos elegidos
const Candidatos = [
    "clase[0].nombre": 0,
    "clase[5].nombre": 0,
    clase[7].nombre => 0,

];

function

