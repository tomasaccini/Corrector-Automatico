var lista_tdas = ["General", "TP0", "VD", "Pila", "Cola", "Lista", "Hash", "Heap", "ABB"];

var correcciones = "1-Error general 1-General-Solución 1\n\
2-Error general 2-General-Solución 2\n\
3-Error TP0 1-TP0-Solución 3\n\
4-Error TP0 2-TP0-Solución 4\n\
5-Error VD 1-VD-Solución 5\n\
6-Error Pila 1-Pila-Solución 6\n\
7-Error General 3-General-Solución 7";

var agrupacion_TDA = {};
var soluciones = {};

function start(){
  loadSolutions();
  loadCheckBoxs();
}


// soluciones[error_code] = [error, solucion]
// agrupacion_TDA[tda] = lista(error_codes de dicho tda)
function loadSolutions() {
  var lineas = correcciones.split("\n");
  for(var i = 0; i < lineas.length; i++){
    var linea = lineas[i].split('-');
    soluciones[linea[0]] = [linea[1], linea[3]];
    if(!agrupacion_TDA[linea[2]]){
      agrupacion_TDA[linea[2]] = [];
    }
    agrupacion_TDA[linea[2]].push(linea[0]);
  }
}

function loadCheckBoxs(){
  for(tda in agrupacion_TDA){
    var lista_errores = agrupacion_TDA[tda];
    for(var i = 0; i < lista_errores.length; i++){
      var error_id = lista_errores[i];
      var error = soluciones[error_id][0];
      var solution = soluciones[error_id][1];
      createCheckbox(error_id, error, tda);
      createSolution(error_id, error, solution);
    }
  }
}

function createCheckbox(error_id, error, tda){
  var container = document.getElementById('containerErrors');


  var checkbox = document.createElement('input');
  checkbox.type = "checkbox";
  checkbox.class = "form-check-input " + tda;
  checkbox.id = error_id+"checkBox";
  checkbox.value = error;
  checkbox.style.display = "block";


  var label = document.createElement('label');
  label.class = "form-check-label " + tda;
  label.innerHTML = error;
  label.for = error_id+"checkBox";
  label.id = error_id+"label";
  label.style.display = "block";

  container.appendChild(checkbox);
  container.appendChild(label);
}

function createSolution(error_id, error, solution){
  var container = document.getElementById('containerSolutions');
  var p = document.createElement('p');
  p.style.display = "none";
  p.id = error_id+"p";
  p.innerHTML = "- <b>" + error + ":</b> " + solution;
  container.appendChild(p);

}

function generateMail(){
  for(error_code in soluciones){
    var cb = document.getElementById(error_code+"checkBox");
    var p = document.getElementById(error_code + 'p');
    if (cb.checked){
      p.style.display = "block";
    } else {
      p.style.display = "none";
    }
  }
}

function refreshErrors(){

  for(var i = 0; i < lista_tdas.length; i++){
    var tda = lista_tdas[i];
    var error_codes = agrupacion_TDA[tda];
    if (!error_codes) continue;
    console.log(error_codes);
    var tda_cb = document.getElementById(tda);

    for(var j = 0; j < error_codes.length; j++){
      actual_error_code = error_codes[j];
      var error_cb = document.getElementById(actual_error_code+"checkBox");
      var error_label = document.getElementById(actual_error_code+"label");
      var p = document.getElementById(actual_error_code + 'p');
      if (tda_cb.checked) {
        error_cb.style.display = "block";
        error_label.style.display = "block";
      } else {
        error_cb.style.display = "none";
        error_cb.checked = false;
        error_label.style.display = "none";
        p.style.display = "none";
      }

    }
  }
}
