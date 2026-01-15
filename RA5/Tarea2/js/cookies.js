// Crea o actualiza una cookie
function setCookie(name, value, days, path = "/") {
  let expires = "";

  // Si se especifican días, calcula la fecha de expiración
  if (days) {
    const date = new Date();
    // Convierte los días a milisegundos y los suma a la fecha actual
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    expires = "; expires=" + date.toUTCString();
  }

  // Crea la cookie con nombre, valor, expiración y ruta
  document.cookie = name + "=" + (value || "") + expires + "; path=" + path;
}

// Obtiene el valor de una cookie por su nombre
function getCookie(name) {
  const nameEQ = name + "=";
  const ca = document.cookie.split(";"); // Divide todas las cookies

  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];

    // Elimina espacios iniciales
    while (c.charAt(0) === " ") c = c.substring(1, c.length);

    // Si la cookie empieza por el nombre buscado, devuelve su valor
    if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
  }

  // Si no existe, devuelve null
  return null;
}

// Se elimina la cookie pasada como parámetro estableciendo su tiempo de vida en negativo
function deleteCookie(name, path = "/") {
  document.cookie = name + "=; Max-Age=-99999999; path=" + path;
}
