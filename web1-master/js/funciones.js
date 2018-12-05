var usuario = "test@test.com";
var contra = "test";
function validateLogin(){
	var user = document.getElementById('username').value;//el value es para forms
	var pwd = document.getElementById('pwd').value;

	if(user==usuario && pwd==contra){
		//pasar a la siguietne pagina
		var dir = 'miCuenta.html';
		window.parent.location.href = "miCuenta.html";
		console.log(window.location.href);
	}else{
		alert('Usuario o contraseña incorrecta.');
	}
}


function sucribir(){
	window.location ="suscripcion.html";
}
var contador = 1;

function addQuestion(){
	var nodoPadre = document.getElementById('tabla1');
	
	var row = document.createElement('tr');

	var tdNumPregunta = document.createElement('td');
	var tdPregunta = document.createElement('td');
	var tdOpciones = document.createElement('td');
	var tdOpcionCorrecta = document.createElement('td');
	var tdEliminar = document.createElement('td');

	var txtNumPregunta = document.createTextNode(contador);
	var txtPregunta = document.createElement('input');
	var divOpciones = document.createElement('div');
	var txtOpcionCorrecta = document.createElement('input');
	var btnEliminar = document.createElement('button');

	txtPregunta.setAttribute("type", "textarea");
	txtPregunta.setAttribute("id", "p"+contador);

	txtOpcionCorrecta.setAttribute("type", "textarea");
	txtOpcionCorrecta.setAttribute("id", "r"+contador)

	btnEliminar.setAttribute("value", "Eliminar");
	btnEliminar.setAttribute("name", "Eliminar");
	btnEliminar.innerHTML = "Eliminar pregunta";
	btnEliminar.onclick = function(){
		//eliminar esto
		nodoPadre.removeChild(btnEliminar.parentNode.parentNode);
	}

	var txtOpcionA = document.createElement('span');
	txtOpcionA.appendChild(document.createTextNode('A) '));
	var inputOpcionA = document.createElement('input');
	inputOpcionA.setAttribute("type", "textarea");

	var txtOpcionB = document.createElement('span');
	txtOpcionB.appendChild(document.createTextNode('B) '));
	var inputOpcionB = document.createElement('input');
	inputOpcionB.setAttribute("type", "textarea");

	var txtOpcionC = document.createElement('span');
	txtOpcionC.appendChild(document.createTextNode('C) '));
	var inputOpcionC = document.createElement('input');
	inputOpcionC.setAttribute("type", "textarea");

	var txtOpcionD = document.createElement('span');
	txtOpcionD.appendChild(document.createTextNode('D) '));
	var inputOpcionD = document.createElement('input');
	inputOpcionD.setAttribute("type", "textarea");

	var txtOpcionE = document.createElement('span');
	txtOpcionE.appendChild(document.createTextNode('E) '));
	var inputOpcionE = document.createElement('input');
	inputOpcionE.setAttribute("type", "textarea");

	var divOpc1 = document.createElement('div');
	var divOpc2 = document.createElement('div');
	var divOpc3 = document.createElement('div');
	var divOpc4 = document.createElement('div');
	var divOpc5 = document.createElement('div');

	divOpc1.appendChild(txtOpcionA);
	divOpc1.appendChild(inputOpcionA);

	divOpc2.appendChild(txtOpcionB);
	divOpc2.appendChild(inputOpcionB);

	divOpc3.appendChild(txtOpcionC);
	divOpc3.appendChild(inputOpcionC);

	divOpc4.appendChild(txtOpcionD);
	divOpc4.appendChild(inputOpcionD);
	
	divOpc5.appendChild(txtOpcionE);
	divOpc5.appendChild(inputOpcionE);

	divOpciones.appendChild(divOpc1);
	divOpciones.appendChild(divOpc2);
	divOpciones.appendChild(divOpc3);
	divOpciones.appendChild(divOpc4);
	divOpciones.appendChild(divOpc5);

	tdNumPregunta.appendChild(txtNumPregunta);
	tdPregunta.appendChild(txtPregunta);
	tdOpciones.appendChild(divOpciones);
	tdOpcionCorrecta.appendChild(txtOpcionCorrecta);
	tdEliminar.appendChild(btnEliminar);

	row.appendChild(tdNumPregunta);
	row.appendChild(tdPregunta);
	row.appendChild(tdOpciones);
	row.appendChild(tdOpcionCorrecta);
	row.appendChild(tdEliminar);

	nodoPadre.appendChild(row);

	contador+=1;
}

$(document).ready(function () {
    $('.navbar-nav li a').click(function(e) {
    	//remove from the pre-existing active classes
        $('.navbar-nav li.active').removeClass('active');

        var $parent = $(this).parent();
        $parent.addClass('active');

        //load the page that the link was pointing to
        $('#content').load($(this).find(a).attr('href')); 

        e.preventDefault();
    });
});