// Inicializa la página de inicio (index.html)
function initIndex() {
  // Uso lógico de getElementsByTagName:
  // Ejemplo: resaltar todos los párrafos del index añadiendo una clase
  const paragraphs = document.getElementsByTagName("p");
  for (let p of paragraphs) {
    p.classList.add("texto-index");
    // No afecta a nada, simplemente demuestra el uso correcto del método
  }

  // Obtiene la cookie de la última visita
  const lastVisit = getCookie("ultima_visita");

  const message = document.getElementById("message");

  // Muestra un mensaje distinto según si es la primera visita o no
  if (lastVisit) {
    message.textContent = `¡Bienvenido de nuevo! Su ultima visita fue el ${lastVisit}`;
  } else {
    message.textContent = `Bienvenido por primera vez al portal.`;
  }

  // Obtiene la fecha y hora actual
  const now = new Date().toLocaleString("es-ES");

  setCookie("ultima_visita", now, 30, "/");

  const btnBorrar = document.getElementById("borrar-datos");

  // Botón para borrar todas las cookies guardadas
  if (btnBorrar) {
    btnBorrar.addEventListener("click", function () {
      deleteCookie("ultima_visita", "/");
      deleteCookie("provincia", "/");
      deleteCookie("turno", "/");
      deleteCookie("carrito", "/");

      alert("Todos los datos han sido eliminados");

      window.location.reload();
    });
  }
}

// Nombre del formulario de registro
const form = "registro_form";

// Carga preferencias guardadas en cookies (provincia y turno)
function cargaPreferencias() {
  const provincia = getCookie("provincia");
  const turno = getCookie("turno");

  // Rellena la provincia si existe cookie
  if (provincia) {
    const selectProvincia = document.getElementById("provincia");
    if (selectProvincia) selectProvincia.value = provincia;
  }

  // Marca el turno si existe cookie
  if (turno) {
    const radioTurno = document.querySelector(
      `input[name='turno'][value='${turno}']`
    );
    if (radioTurno) radioTurno.checked = true;
  }
}

// Guarda preferencias si el usuario marcó "recordar"
function guardarPreferencias(form) {
  const recordarCheck = document.getElementById("recordar");

  if (recordarCheck && recordarCheck.checked) {
    const provincia = document.getElementById("provincia").value;

    const turno = form.elements["turno"].value;

    if (provincia) setCookie("provincia", provincia, 7, "/");
    if (turno) setCookie("turno", turno, 7, "/");
  } else {
    // Si no quiere recordar, se borran las cookies
    deleteCookie("provincia", "/");
    deleteCookie("turno", "/");
  }
}

// Inicializa la página de registro (registro.html)
function initRegistro() {
  const form = document.forms["registro-form"];

  if (!form) return;

  // Carga preferencias guardadas
  cargaPreferencias(form);

  // Validación del formulario al enviar
  form.addEventListener("submit", (e) => {
    if (!validarFormulario(form)) {
      console.log("Envio cancelado debido a errores en el formulario");
      e.preventDefault();
    } else {
      guardarPreferencias(form);
      alert("Formulario enviado");
      e.preventDefault();
    }
  });

  // Validación en tiempo real (blur y change)
  for (const element of form.elements) {
    if (
      element.tagName === "INPUT" ||
      element.tagName === "TEXTAREA" ||
      element.tagName === "SELECT"
    ) {
      const needsValidation =
        element.required ||
        [
          "email",
          "matricula",
          "password",
          "telefono",
          "provincia",
          "condiciones",
        ].includes(element.id);

      if (needsValidation) {
        element.addEventListener("blur", function () {
          validarCampo(this);
        });
      }

      if (element.id === "provincia") {
        element.addEventListener("change", function () {
          validarCampo(this);
        });
      }
    }
  }

  // Botón de validación manual
  const btnValidar = document.getElementById("btn-validar");
  if (btnValidar) {
    btnValidar.addEventListener("click", function () {
      if (validarFormulario(form)) {
        alert("La validación manual ha sido exitosa.");
      } else {
        alert("La validación manual ha detectado errores. Revísalos.");
      }
    });
  }

  // Generación de token oculto
  const token =
    Math.random().toString(36).substring(2, 15) +
    Math.random().toString(36).substring(2, 15);

  const hiddenToken = document.getElementById("token");
  if (hiddenToken) hiddenToken.value = token;

  // Elementos para demostración de burbujeo/captura de eventos
  const bubbleContainer = document.getElementById("bubble-container");
  const bubbleButton = document.getElementById("bubble-button");
  const stopPropagationCheck = document.getElementById(
    "stop-propagation-check"
  );
  const log = document.getElementById("event-log");

  // Función para registrar eventos en pantalla
  const logEvent = (msg) => {
    const p = document.createElement("p");
    p.textContent = msg;
    log.appendChild(p);
  };

  // Fase de captura
  bubbleContainer.addEventListener(
    "click",
    function (e) {
      logEvent(
        "1. Contenedor CLICK (Fase de **Captura**) - target: " +
          e.target.tagName
      );
    },
    true
  );

  // Evento en el botón (fase target)
  bubbleButton.addEventListener("click", function (e) {
    logEvent("2. Botón CLICK (Fase de **Burbujeo** - TARGET)");

    if (stopPropagationCheck && stopPropagationCheck.checked) {
      e.stopPropagation();
      logEvent("2b. stopPropagation() ejecutado.");
    }
  });

  // Fase de burbujeo
  bubbleContainer.addEventListener(
    "click",
    function (e) {
      logEvent(
        "3. Contenedor CLICK (Fase de **Burbujeo**) - target: " +
          e.target.tagName
      );
    },
    false
  );
}

// Obtiene el carrito desde la cookie y lo convierte en objeto
function getCarrito() {
  const cookie = getCookie("carrito");
  if (!cookie) return {};

  const carrito = {};
  const items = cookie.split("|");

  items.forEach((item) => {
    if (item) {
      const [id, cantidad] = item.split(":");
      carrito[id] = parseInt(cantidad, 10);
    }
  });

  return carrito;
}

// Guarda el carrito en una cookie
function saveCarrito(carrito) {
  const items = [];

  for (const id in carrito) {
    if (carrito[id] > 0) {
      items.push(`${id}:${carrito[id]}`);
    }
  }

  const cookieValue = items.join("|");
  setCookie("carrito", cookieValue, 365, "/");
}

// Muestra el contenido del carrito en pantalla
function displayCarrito() {
  const carrito = getCarrito();
  const carritoDiv = document.getElementById("carrito-contenido");
  const totalElement = document.getElementById("carrito-total");

  let total = 0;
  let html = "<h3>Contenido del Carrito</h3>";

  // Si está vacío
  if (Object.keys(carrito).length === 0) {
    html += "<p>El carrito está vacío.</p>";
    totalElement.textContent = "0.00€";
    carritoDiv.innerHTML = html;
    return;
  }

  html += "<ul>";

  // Recorre cada producto del carrito
  for (const id in carrito) {
    const cantidad = carrito[id];
    const row = document.getElementById(`taller-${id}`);

    if (row) {
      const nombre = row.dataset.nombre;
      const precio = parseFloat(row.dataset.precio);
      const subtotal = cantidad * precio;

      html += `<li>**${nombre}** (x${cantidad}) - ${subtotal.toFixed(2)}€</li>`;
      total += subtotal;
    }
  }

  html += "</ul>";

  carritoDiv.innerHTML = html;
  totalElement.textContent = total.toFixed(2) + "€";
}

// Añade un ítem al carrito
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

// Inicializa la página de talleres (talleres.html)
function initTalleres() {
  displayCarrito();

  const tallerList = document.getElementById("taller-list");

  // Maneja clics en botones "añadir al carrito"
  if (tallerList) {
    tallerList.addEventListener("click", function (e) {
      const btn = e.target.closest(".add-to-cart");

      if (btn) {
        const id = btn.dataset.tallerId;
        const row = document.getElementById(`taller-${id}`);
        const inputCantidad = row
          ? row.querySelector('input[type="number"]')
          : null;

        if (inputCantidad) {
          const cantidad = inputCantidad.value;

          if (parseInt(cantidad) > 0) {
            addItemToCarrito(id, cantidad);
            inputCantidad.value = 1;
          } else {
            alert("Por favor, introduce una cantidad válida.");
          }
        }
      }
    });
  }

  // Botón para vaciar carrito
  const btnVaciar = document.getElementById("vaciar-carrito");
  if (btnVaciar) {
    btnVaciar.addEventListener("click", function () {
      deleteCookie("carrito", "/");
      displayCarrito();
      alert("El carrito ha sido vaciado.");
    });
  }

  // Campo de búsqueda, muestra el log en la consola
  const searchInput = document.getElementById("taller-search");
  if (searchInput) {
    searchInput.addEventListener("keyup", function () {
      console.log("Evento keyup disparado en el campo de búsqueda.");
    });
  }
}

// Detecta qué página se está cargando y ejecuta su inicializador
window.addEventListener("load", function () {
  const path = window.location.pathname;

  if (path.endsWith("index.html") || path === "/") {
    initIndex();
  } else if (path.endsWith("registro.html")) {
    initRegistro();
  } else if (path.endsWith("talleres.html")) {
    initTalleres();
  }
});
