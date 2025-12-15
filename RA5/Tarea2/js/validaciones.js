document.addEventListener("DOMContentLoaded", () => {

    const validarFormulario = {

        validarTexto: (campo) => {

            return campo !== "";

        },

        validarMatricula: (campo) => {

            regex = "(^\d{4}\s?[A-Z]{3}$)"

            return regex.test(campo)

        }
        ,

        validarEmail: (campo) => {

            regex = "^[a-zA-Z0-9]@[a-zA-Z].[a-zA-Z]{3}";

            return regex.test(campo);

        },
        validarTelefono: (campo) => {

            regex = "^[0-9]{9}";

            return regex.test(campo)

        },

        validadPassword: (campo1, campo2) => {

            regex = "^[a-zA-Z0-9]{8,}";

            if (campo1 !== "" && campo2 !== "") {

                if (regex.test(campo1) && regex.test(campo2)) {

                    if (campo1 !== campo2) {

                        return false;

                    } else {

                        return true;

                    }

                } else {

                    return false;

                }

            } else {

                return true;

            }

        }, validarProvincia: (campo) => {

            return selectedIndex === 0;

        }

    }

})