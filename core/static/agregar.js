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
    if(3 <= nom.value.length && con.value.length <= 10){
        con.classList.remove("error");
    }else{
        con.classList.add("error");
    }
}

function borrar(){
    document.querySelector("#borrar").value = "";
}

function agregar(){
    document.querySelector("#agregar").value = "";
}

function eliminar(){
    document.querySelector("#eliminar").value = "";
}

function modificar(){
    document.querySelector("#modificar").value = "";
}