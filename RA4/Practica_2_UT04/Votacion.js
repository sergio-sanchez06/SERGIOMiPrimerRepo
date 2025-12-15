class Alumno {
            constructor(nombre) {
                this.nombre = nombre;
                this.haVotado = false;
            }

            /**
             * Simula la acción de votar.
             * @param {string} candidatoId - El identificador del candidato elegido.
             * @returns {string} Mensaje de confirmación del voto.
             */
            emitirVoto(candidatoId) {
                if (!this.haVotado) {
                    this.haVotado = true;
                    return candidatoId;
                } else {
                    return null; // Ya ha votado
                }
            }
        }

        // --- LÓGICA DE VOTACIÓN DELEGADO ---

        // Simulación de carga desde un 'fichero' (array de objetos Alumno)
        // En una aplicación real, esta información se cargaría de una base de datos o archivo JSON.
        const AlumnosData = [
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
            { id: 'C1', nombre: 'Candidato 1 (María)' },
            { id: 'C2', nombre: 'Candidato 2 (Pedro)' },
            { id: 'C3', nombre: 'Candidato 3 (Sofía)' },
        ];

        const Votacion = {
            alumnos: [...AlumnosData], // Copia para resetear
            candidatos: Candidatos,
            conteoVotos: {},
            votanteActualIndex: 0,
            
            /** Inicializa la votación: reinicia conteo y muestra el primer votante. */
            iniciar: function() {
                this.conteoVotos = {};
                this.votanteActualIndex = 0;
                
                // Inicializar el conteo a cero para todos los candidatos
                this.candidatos.forEach(c => {
                    this.conteoVotos[c.id] = 0;
                });
                
                this.alumnos.forEach(a => a.haVotado = false); // Asegurar que todos puedan votar
                
                this.actualizarUI();
            },

            /** * Procesa el voto del alumno actual.
             * @param {string} candidatoId - ID del candidato votado.
             */
            votar: function(candidatoId) {
                const alumno = this.alumnos[this.votanteActualIndex];
                
                if (alumno) {
                    const voto = alumno.emitirVoto(candidatoId);
                    
                    if (voto) {
                        this.conteoVotos[voto]++;
                        this.siguienteVotante();
                    }
                }
            },

            /** Avanza al siguiente votante o finaliza la votación. */
            siguienteVotante: function() {
                this.votanteActualIndex++;
                
                if (this.votanteActualIndex < this.alumnos.length) {
                    this.actualizarUI();
                } else {
                    this.finalizarVotacion();
                }
            },

            /** Determina los resultados (delegado, subdelegado) y maneja empates. */
            finalizarVotacion: function() {
                // 1. Ocultar la sección de votación y mostrar la de resultados
                document.getElementById('voting-section').classList.add('hidden');
                document.getElementById('results-section').classList.remove('hidden');
                document.getElementById('repeat-button').classList.add('hidden');
                
                // 2. Convertir el conteo en un array para ordenar
                const resultados = Object.entries(this.conteoVotos).map(([id, votos]) => {
                    const nombre = this.candidatos.find(c => c.id === id).nombre;
                    return { id, nombre, votos };
                });

                // 3. Ordenar por votos de forma descendente
                resultados.sort((a, b) => b.votos - a.votos);

                const delegado = resultados[0];
                const subdelegado = resultados[1];
                
                // 4. Determinar si hay empate
                let hayEmpateDelegado = resultados.length > 1 && delegado.votos === subdelegado.votos;
                let hayEmpateSubdelegado = resultados.length > 2 && subdelegado.votos === resultados[2].votos;

                // 5. Mostrar resultados
                this.mostrarConteoVotos(resultados);
                this.mostrarCargos(delegado, subdelegado, hayEmpateDelegado, hayEmpateSubdelegado);

                // 6. Activar botón de repetición si hay empate
                if (hayEmpateDelegado || hayEmpateSubdelegado) {
                    document.getElementById('repeat-button').classList.remove('hidden');
                }
            },
            
            /** Resetea la votación para un desempate. */
            resetearVotacion: function() {
                // Reiniciar el estado de la votación
                this.votanteActualIndex = 0;
                this.conteoVotos = {};
                this.alumnos.forEach(a => a.haVotado = false);
                
                // Ocultar resultados y mostrar votación
                document.getElementById('results-section').classList.add('hidden');
                document.getElementById('voting-section').classList.remove('hidden');
                
                // Volver a iniciar para actualizar la UI
                this.iniciar();
                document.getElementById('repeat-button').classList.add('hidden');
            },

            /** * Actualiza el display del votante actual y la barra de progreso. 
             */
            actualizarUI: function() {
                const totalAlumnos = this.alumnos.length;
                const alumnoActual = this.alumnos[this.votanteActualIndex];
                
                // Mostrar el nombre del votante actual
                document.getElementById('current-voter').innerHTML = `Es el turno de votar de: <span class="text-indigo-800 font-bold">${alumnoActual.nombre}</span>`;

                // Actualizar barra de progreso
                document.getElementById('progress-bar').textContent = `Progreso: ${this.votanteActualIndex} / ${totalAlumnos} votos completados.`;
            },

            /** * Muestra el conteo detallado de votos.
             * @param {Array<Object>} resultados - Array ordenado de los candidatos.
             */
            mostrarConteoVotos: function(resultados) {
                const countsDiv = document.getElementById('vote-counts');
                countsDiv.innerHTML = '';
                resultados.forEach(res => {
                    countsDiv.innerHTML += `
                        <p class="flex justify-between items-center text-gray-700">
                            <span class="font-medium">${res.nombre}</span>
                            <span class="px-3 py-1 bg-gray-200 text-gray-800 font-bold rounded-full">${res.votos} votos</span>
                        </p>
                    `;
                });
            },

            /** * Muestra quién es el delegado y subdelegado, incluyendo avisos de empate.
             */
            mostrarCargos: function(delegado, subdelegado, hayEmpateDelegado, hayEmpateSubdelegado) {
                const delegadoDiv = document.getElementById('final-delegate');
                const subdelegadoDiv = document.getElementById('final-subdelegate');

                // Mostrar Delegado
                if (hayEmpateDelegado) {
                    delegadoDiv.className = "text-xl font-semibold mb-3 text-red-600";
                    delegadoDiv.textContent = `DELEGADO: ⚠️ EMPATE por la primera posición con ${delegado.votos} votos.`;
                } else {
                    delegadoDiv.className = "text-xl font-semibold mb-3 text-green-700";
                    delegadoDiv.textContent = `DELEGADO(A) ELEGIDO(A): ${delegado.nombre} con ${delegado.votos} votos. 🎉`;
                }

                // Mostrar Subdelegado
                if (hayEmpateSubdelegado && !hayEmpateDelegado) { // Solo si no hubo empate delegado
                    subdelegadoDiv.className = "text-xl font-semibold mb-4 text-red-600";
                    subdelegadoDiv.textContent = `SUBDELEGADO: ⚠️ EMPATE por la segunda posición con ${subdelegado.votos} votos.`;
                } else if (!hayEmpateDelegado) {
                    subdelegadoDiv.className = "text-xl font-semibold mb-4 text-green-600";
                    subdelegadoDiv.textContent = `SUBDELEGADO(A) ELEGIDO(A): ${subdelegado.nombre} con ${subdelegado.votos} votos.`;
                } else {
                    subdelegadoDiv.textContent = "SUBDELEGADO: Posición no determinada debido al empate de Delegado.";
                }
            },
            
            /** Configura los botones de los candidatos al iniciar la aplicación. */
            configurarBotones: function() {
                const buttonsDiv = document.getElementById('candidate-buttons');
                buttonsDiv.innerHTML = '';
                this.candidatos.forEach(c => {
                    const button = document.createElement('button');
                    button.textContent = c.nombre;
                    button.className = 'py-3 px-4 bg-indigo-600 text-white font-bold rounded-lg shadow-md hover:bg-indigo-700 transition-colors transform hover:scale-105';
                    button.onclick = () => this.votar(c.id);
                    buttonsDiv.appendChild(button);
                });
            }
        };

        // --- Inicialización ---

        document.addEventListener('DOMContentLoaded', () => {
            Votacion.configurarBotones();
            Votacion.iniciar();
        });