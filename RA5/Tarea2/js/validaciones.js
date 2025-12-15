// js/validaciones.js

// Expresiones regulares obligatorias
const REGEXP_EMAIL = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/; // Literal
const REGEXP_MATRICULA = new RegExp(/^\d{4}\s?[A-Z]{3}$/); // Constructor
const REGEXP_PASS = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/; // Mín. 8 chars, mayús, minús, número

/**
 * Marca visualmente un campo como correcto o incorrecto.
 * @param {HTMLElement} element - El elemento del formulario.
 * @param {boolean} isValid - True si es válido, False si es inválido.
 */
function marcarCampo(element, isValid) {
    element.classList.remove('error', 'ok');
    if (isValid) {
        element.classList.add('ok');
    } else {
        element.classList.add('error');
    }
}

/**
 * Valida un campo específico y marca el resultado.
 * @param {HTMLElement} campo - El elemento del formulario a validar.
 * @returns {boolean} - True si el campo es válido, False en caso contrario.
 */
function validarCampo(campo) {
    let isValid = true;
    const value = campo.value.trim();
    const id = campo.id;

    if (campo.required && value === '') {
        isValid = false;
    } else if (id === 'email') {
        isValid = REGEXP_EMAIL.test(value);
    } else if (id === 'matricula') {
        isValid = REGEXP_MATRICULA.test(value.toUpperCase()); // Convertir a mayúsculas para la validación
    } else if (id === 'password') {
        isValid = REGEXP_PASS.test(value);
    } else if (id === 'telefono') {
        isValid = /^\d{9}$/.test(value); // Teléfono numérico de 9 dígitos
    } else if (id === 'provincia') {
        // Validar que no sea la opción inicial (selectedIndex == 0)
        isValid = campo.selectedIndex !== 0;
    } else if (id === 'condiciones') {
        // Validar el checkbox de condiciones (obligatorio)
        isValid = campo.checked;
    }

    marcarCampo(campo, isValid);
    return isValid;
}

/**
 * Función que realiza la validación de todo el formulario.
 * @param {HTMLFormElement} form - El elemento formulario.
 * @returns {boolean} - True si todo es válido, False si hay errores.
 */
function validarFormulario(form) {
    // 1. Limpieza inicial de errores
    limpiarErrores(form);

    let isFormValid = true;
    let firstErrorField = null; // Para enfocar el primer error

    // 2. Validación de todos los elementos requeridos y con validación específica
    for (const element of form.elements) {
        if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA' || element.tagName === 'SELECT') {
            const needsValidation = element.required || ['email', 'matricula', 'password', 'telefono', 'provincia', 'condiciones'].includes(element.id);
            if (needsValidation) {
                const isValid = validarCampo(element);
                if (!isValid) {
                    isFormValid = false;
                    if (!firstErrorField) {
                        firstErrorField = element;
                    }
                }
            }
        }
    }

    // 3. Validación de coherencia de contraseñas
    const pass = document.getElementById('password');
    const repeatPass = document.getElementById('repeat-password');
    if (pass && repeatPass) {
        const arePasswordsCoherent = pass.value === repeatPass.value && REGEXP_PASS.test(pass.value);
        marcarCampo(repeatPass, arePasswordsCoherent);
        if (!arePasswordsCoherent) {
            isFormValid = false;
            if (!firstErrorField) {
                 // Si la validación de 'password' pasó, pero la de coherencia falló, enfocar repetición.
                firstErrorField = repeatPass;
            }
        }
    }

    // 4. Enfocar el primer campo con error
    if (firstErrorField) {
        firstErrorField.focus();
    }

    return isFormValid;
}

/**
 * Recorre form.elements para limpiar las clases de error/ok.
 * @param {HTMLFormElement} form - El elemento formulario.
 */
function limpiarErrores(form) {
    for (const element of form.elements) {
        element.classList.remove('error', 'ok');
    }
}