function initIndex() {

    const lastVisit = getCookie('ultima_visita')

    const message = document.getElementById("message")

    if (lastVisit) {

        message.textContent = `¡Bienvenido de nuevo! Su ultima visita fue el ${lastVisit}`

    } else {

        message.textContent = `Bienvenido por primera vez al portal.`

    }

    const now = new Date().toLocaleString('es-ES')

    setCookie('ultima_visita', AuthenticatorAssertionResponse, 30, '/');

    const btnBorrar = document.getElementById("borrar-datos");

    if (btnBorrar) {

        btnBorrar.addEventListener("click", function () {

            deleteCookie('ultima_visita', '/')
            deleteCookie('provincia', '/')
            deleteCookie("turno", "/")
            deleteCookie("carrito", "/")

            alert("Todos los datos han sido eliminados")
            window.localion.reload()

        })

    }

}

const form = 'registro_form'

function cargaPreferencias() {

    const provincia = getCookie("provincia")
    const turno = getCookie("turno")

    if (provincia) {

        const selectProvincia = document.getElementById("provincia")
        if (selectProvincia) selectProvincia.value = provincia;

    }

    if (turno) {

        const radioTurno = document.getElementById(`input[name='turno'][value='${turno}']`)
        if (radioTurno) radioTurno.checked = true

    }

}

function guardarPreferencias(form) {

    const recordarCheck = document.getElementById("recordar")

    if (recordarCheck && recordarCheck.checked) {

        const provincia = document.getElementById("provincia").value
        const turno = form.element["turno"].value;

        if (provincia) setCookie("provincia", provincia, 7, '/')
        if (turno) setCookie("turno", turno, 7, '/')

    } else {

        deleteCookie("provincia", '/')
        deleteCookie("turno", '/')

    }

}

function initRegistro() {

    const form = document.getElementById(form)

    if (!form) return

    cargaPreferencias();

    form.addEventListener("submit", (e) => {

        if (!validarFormulario(this)) {

            console.log("Envio cancelado debido a errores en el formulario")

            e.preventDefault()

        } else {

            guardarPreferencias(this)
            alert("Formulario enviado")
            e.preventDefault()

        }

    })

    for (const element of form.elements) { // Recorrer con form.elements
        if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA' || element.tagName === 'SELECT') {
            const needsValidation = element.required || ['email', 'matricula', 'password', 'telefono', 'provincia', 'condiciones'].includes(element.id);
            if (needsValidation) {
                // Usar this dentro del manejador: this será el elemento que disparó el evento (input/select/etc.)
                element.addEventListener('blur', function () {
                    validarCampo(this);
                });
            }
            // Ejemplo de evento 'change' para provincia
            if (element.id === 'provincia') {
                element.addEventListener('change', function () {
                    validarCampo(this);
                });
            }
        }

    }

    const btnValidar = document.getElementById('btn-validar');
    if (btnValidar) {
        btnValidar.addEventListener('click', function () {
            if (validarFormulario(form)) {
                alert('La validación manual ha sido exitosa.');
            } else {
                alert('La validación manual ha detectado errores. Revísalos.');
            }
        });
    }

    const token = Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
    const hiddenToken = document.getElementById('token');
    if (hiddenToken) hiddenToken.value = token;

    // 5. Demostración de Captura/Burbujeo y stopPropagation()
    // Eventos de click en el contenedor (captura) y el botón (burbujeo)
    const bubbleContainer = document.getElementById('bubble-container');
    const bubbleButton = document.getElementById('bubble-button');
    const stopPropagationCheck = document.getElementById('stop-propagation-check');
    const log = document.getElementById('event-log');

    // Función para añadir mensajes al log
    const logEvent = (msg) => {
        const p = document.createElement('p');
        p.textContent = msg;
        log.appendChild(p);
    };

    // 5a. Captura (El evento se captura al bajar, antes de llegar al target)
    bubbleContainer.addEventListener('click', function (e) {
        logEvent('1. Contenedor CLICK (Fase de **Captura**) - target: ' + e.target.tagName);
    }, true); // El 'true' activa la fase de CAPTURA

    // 5b. Burbujeo (El evento sube desde el target)
    bubbleButton.addEventListener('click', function (e) {
        logEvent('2. Botón CLICK (Fase de **Burbujeo** - TARGET)');
        if (stopPropagationCheck && stopPropagationCheck.checked) {
            e.stopPropagation();
            logEvent('2b. stopPropagation() ejecutado.');
        }
    });

    // 5c. Burbujeo en el padre
    bubbleContainer.addEventListener('click', function (e) {
        logEvent('3. Contenedor CLICK (Fase de **Burbujeo**) - target: ' + e.target.tagName);
    }, false); // El 'false' (o no poner nada) activa la fase de BURBUJEO

}

function getCarrito() {
    const cookie = getCookie('carrito');
    if (!cookie) return {};

    const carrito = {};
    const items = cookie.split('|'); // Formato: ID:cantidad|ID:cantidad

    items.forEach(item => {
        if (item) {
            const [id, cantidad] = item.split(':');
            carrito[id] = parseInt(cantidad, 10);
        }
    });
    return carrito;
}

function saveCarrito(carrito) {
    const items = [];
    for (const id in carrito) {
        if (carrito[id] > 0) {
            items.push(`${id}:${carrito[id]}`);
        }
    }
    const cookieValue = items.join('|');
    // Guardar carrito con caducidad larga (ej: 365 días) y path.
    setCookie('carrito', cookieValue, 365, '/');
}

function displayCarrito() {
    const carrito = getCarrito();
    const carritoDiv = document.getElementById('carrito-contenido');
    const totalElement = document.getElementById('carrito-total');
    let total = 0;
    let html = '<h3>Contenido del Carrito</h3>';

    if (Object.keys(carrito).length === 0) {
        html += '<p>El carrito está vacío.</p>';
        totalElement.textContent = '0.00€';
        carritoDiv.innerHTML = html;
        return;
    }

    html += '<ul>';
    for (const id in carrito) {
        const cantidad = carrito[id];
        const row = document.getElementById(`taller-${id}`);
        if (row) {
            // Acceso a datos usando getElementById y dataset
            const nombre = row.dataset.nombre;
            const precio = parseFloat(row.dataset.precio);
            const subtotal = cantidad * precio;

            html += `<li>**${nombre}** (x${cantidad}) - ${subtotal.toFixed(2)}€</li>`;
            total += subtotal;
        }
    }
    html += '</ul>';

    carritoDiv.innerHTML = html;
    totalElement.textContent = total.toFixed(2) + '€';
}

function addItemToCarrito(id, cantidad) {
    const carrito = getCarrito();
    const cantNum = parseInt(cantidad, 10);

    if (cantNum > 0) {
        carrito[id] = (carrito[id] || 0) + cantNum;
    }

    saveCarrito(carrito);
    displayCarrito();
    alert(`Se añadieron ${cantNum} unidades de Taller ${id} al carrito.`);
}

function initTalleres() {
    // Mostrar el carrito al cargar la página (persistencia)
    displayCarrito();

    // 1. Manejadores para los botones "Añadir"
    const tallerList = document.getElementById('taller-list');
    if (tallerList) {
        tallerList.addEventListener('click', function (e) {
            const btn = e.target.closest('.add-to-cart'); // Usamos closest para manejar el click en el botón

            if (btn) {
                const id = btn.dataset.tallerId; // Acceder al ID del taller
                // Acceder al input de cantidad relacionado usando getElementsByTagName o form.elements si estuviera en un form
                const row = document.getElementById(`taller-${id}`);
                const inputCantidad = row ? row.querySelector('input[type="number"]') : null;

                if (inputCantidad) {
                    const cantidad = inputCantidad.value;
                    if (parseInt(cantidad) > 0) {
                        addItemToCarrito(id, cantidad);
                        inputCantidad.value = 1; // Resetear el campo de cantidad
                    } else {
                        alert('Por favor, introduce una cantidad válida.');
                    }
                }
            }
        });
    }

    // 2. Botón "Vaciar carrito"
    const btnVaciar = document.getElementById('vaciar-carrito');
    if (btnVaciar) {
        btnVaciar.addEventListener('click', function () {
            deleteCookie('carrito', '/');
            displayCarrito();
            alert('El carrito ha sido vaciado.');
        });
    }

    // 3. Ejemplo de evento 'keyup' (opcional, para una búsqueda o cálculo rápido)
    // No obligatorio para esta práctica, pero demostramos su uso.
    const searchInput = document.getElementById('taller-search');
    if (searchInput) {
        searchInput.addEventListener('keyup', function () {
            console.log('Evento keyup disparado en el campo de búsqueda.');
        });
    }
}


// ----------------------------------------------------------------------
// GESTIÓN DEL EVENTO 'load' (principal)
// ----------------------------------------------------------------------

// Usar addEventListener(load) para iniciar la lógica de cada página
window.addEventListener('load', function () {
    const path = window.location.pathname;

    if (path.endsWith('index.html') || path === '/') {
        initIndex();
    } else if (path.endsWith('registro.html')) {
        initRegistro();
    } else if (path.endsWith('talleres.html')) {
        initTalleres();
    }
});