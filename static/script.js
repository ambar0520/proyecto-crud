
function validarFormulario() {
    const usuario = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (usuario === "" || password === "") {
        alert("Por favor, completa todos los campos.");
        return false;
    }
    return true;
}

function validarUpdate() {
    const usuario = document.getElementById("username").value;
    const nuevaClave = document.getElementById("new_password").value;

    if (usuario === "" || nuevaClave === "") {
        alert("Por favor, completa todos los campos.");
        return false;
    }
    return true;
}

function validarDelete() {
    const usuario = document.getElementById("username").value;

    if (usuario === "") {
        alert("Debes escribir el nombre del usuario a eliminar.");
        return false;
    }
    return true;
}
