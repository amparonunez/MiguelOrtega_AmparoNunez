
function validarRut(){
    var rut = document.querySelector("#rut");
    if(rut.value.length == 9 || rut.value.length == 10){
        rut.classList.remove("error");
    }else{
        rut.classList.add("error");
    }
}

function validarContrasena(){
    var con = document.querySelector("#contrasena");
    if(3 <= con.value.length && con.value.length <= 10){
        con.classList.remove("error");
    }else{
        con.classList.add("error");
    }
}

function iniciarSesion() {
    var rutInput = document.getElementById('rut');
    var contrasenaInput = document.getElementById('contrasena');
    
    if (rutInput.value === '') {
        rutInput.classList.add('error');
    }
    
    if (contrasenaInput.value === '') {
        contrasenaInput.classList.add('error');
    }

    if (rutInput.value !== '' && contrasenaInput.value !== '') {
        // Aquí ira el codigo que te lleva al iniciar sesion
        alert('Iniciando sesión...');
    }
}

// validaciones registro

function validarFormulario() {
    var nombre = document.getElementById("nombre").value;
    if (nombre.trim() === "") {
      alert("Por favor, ingresa tu nombre completo.");
      return false; 
    }

   
    var email = document.getElementById("email").value;
    if (email.trim() === "") {
      alert("Por favor, ingresa tu dirección de email.");
      return false;
    }

    
    var telefono = document.getElementById("telefono").value;
    if (telefono.trim() === "") {
      alert("Por favor, ingresa tu número de teléfono.");
      return false;
    }

   
    var direccion = document.getElementById("direccion").value;
    if (direccion.trim() === "") {
      alert("Por favor, ingresa tu dirección.");
      return false;
    }

    return true;
  }

  