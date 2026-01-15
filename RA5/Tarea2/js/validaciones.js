// Expresión regular para validar emails con formato estándar
const REGEXP_EMAIL = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;

// Expresión regular para validar matrículas españolas (4 números + 3 letras)
const REGEXP_MATRICULA = new RegExp(/^\d{4}\s?[A-Z]{3}$/);

// Expresión regular para validar contraseñas seguras:
// mínimo 8 caracteres, al menos una minúscula, una mayúscula y un número
const REGEXP_PASS = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/;

function marcarCampo(element, isValid) {
  // Limpia clases previas de validación
  element.classList.remove("error", "ok");

  // Marca el campo como válido o inválido
  if (isValid) {
    element.classList.add("ok");
  } else {
    element.classList.add("error");
  }
}

function validarCampo(campo) {
  let isValid = true;
  const value = campo.value.trim(); // Elimina espacios al inicio y final
  const id = campo.id; // Obtiene el id del campo

  // Validación según el tipo de campo
  if (campo.required && value === "") {
    // Si es obligatorio y está vacío → inválido
    isValid = false;
  } else if (id === "email") {
    isValid = REGEXP_EMAIL.test(value);
  } else if (id === "matricula") {
    // Se pasa a mayúsculas antes de validar
    isValid = REGEXP_MATRICULA.test(value.toUpperCase());
  } else if (id === "password") {
    isValid = REGEXP_PASS.test(value);
  } else if (id === "telefono") {
    // Teléfono español de 9 dígitos
    isValid = /^\d{9}$/.test(value);
  } else if (id === "provincia") {
    // Debe seleccionarse una opción distinta a la primera
    isValid = campo.selectedIndex !== 0;
  } else if (id === "condiciones") {
    // Checkbox debe estar marcado
    isValid = campo.checked;
  }

  // Marca visualmente el campo según su validez
  marcarCampo(campo, isValid);
  return isValid;
}

function validarFormulario(form) {
  // Limpia errores previos
  limpiarErrores(form);

  let isFormValid = true;
  let firstErrorField = null; // Variable para almacenar el primer campo con error

  // Recorre todos los elementos del formulario
  for (const element of form.elements) {
    // Solo valida inputs, textareas y selects
    if (
      element.tagName === "INPUT" ||
      element.tagName === "TEXTAREA" ||
      element.tagName === "SELECT"
    ) {
      // Determina si el campo necesita validación
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
        const isValid = validarCampo(element);

        // Si no es válido, se registra
        if (!isValid) {
          isFormValid = false;
          if (!firstErrorField) {
            firstErrorField = element; // Guarda el primer campo con error
          }
        }
      }
    }
  }

  // Validación para comprobar que la contraseña y la contraseña repetida coinciden
  const pass = document.getElementById("password");
  const repeatPass = document.getElementById("repeat-password");

  if (pass && repeatPass) {
    const arePasswordsCoherent =
      pass.value === repeatPass.value && REGEXP_PASS.test(pass.value);

    // Marca el campo de repetir contraseña
    marcarCampo(repeatPass, arePasswordsCoherent);

    if (!arePasswordsCoherent) {
      isFormValid = false;
      if (!firstErrorField) {
        firstErrorField = repeatPass;
      }
    }
  }

  // Se pone el cursor en el primer campo con error
  if (firstErrorField) {
    firstErrorField.focus();
  }

  return isFormValid;
}

function limpiarErrores(form) {
  // Elimina clases de validación de todos los campos
  for (const element of form.elements) {
    element.classList.remove("error", "ok");
  }
}
