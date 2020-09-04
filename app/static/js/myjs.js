/**
 * Verifica si el valor del campo ya se encuentra en la DB
 * @param {*} value Valor a comparar
 * @param {*} field Campo de la tabla
 * @param {*} updateId Id del campo del formulario a ser actualizado
 */
function validateField(value, field, updateId) {
    var url = "/validatefield?field=" + field + "&value=" + value.value;
    
    var request;
    
    if (window.XMLHttpRequest) {
        request = new window.XMLHttpRequest();
    } else {
        request = new window.ActiveXObject("Microsoft.XMLHTTP");
    }
    
    request.open("GET", url, true);
    request.send();
    // console.log(request)
    request.onreadystatechange = function() {
        if (request.readyState == 4 && request.status == 200) {
            if (request.responseText == "Used") {
                console.log("Used")
                document.getElementById(updateId).classList.add("d-block");
            } else {
                console.log("Available")
                document.getElementById(updateId).classList.remove("d-block");
            }
        }
    }
}

/**
 * Verifica si dos contraseñas son iguales
 * @param {*} pass1 
 * @param {*} pass2 
 * @param {*} updateId Id del campo del formulario a ser actualizado
 */
function verifyPasswords(pass1, pass2, updateId) {

    if (pass1.value != "" && pass2.value != "") {
        if (pass1.value == pass2.value) {
            console.log("Las contraseñas coinciden")
            document.getElementById(updateId).classList.remove("d-block");
            return true;
        } else {
            console.log("Las contraseñas NO coinciden")
            document.getElementById(updateId).classList.add("d-block");
            return false;
        }
    } else {
        console.log("Contraseña vacía");
        return false;
    }
}
    