import React from 'react';
import ReactDOM from 'react-dom/client';
import '../../../../../Downloads/asistetareastemp-main/asistetareastemp-main/src/index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

function showSection(sectionId) {
  const sections = document.querySelectorAll('.section');
  sections.forEach(section => section.classList.add('hidden'));
  document.getElementById(sectionId).classList.remove('hidden');
}

function registerUser() {
  alert("Registro exitoso");
  showSection('task-options');
}

function addTask() {
  alert("Tarea agregada exitosamente");
  showSection('task-options');
}

function searchTask() {
  alert("Tareas encontradas");
  showSection('task-results');
}

function deleteTask() {
  const confirmDelete = confirm("¿Está seguro de que desea eliminar esta tarea?");
  if (confirmDelete) {
      alert("Tarea eliminada");
      showSection('task-search');
  }
}

    function buscarTarea() {
        // Capturar las selecciones del usuario
        var materia = document.getElementById('materia').value;
        var grado = document.getElementById('grado').value;
        var destreza = document.getElementById('destreza').value;
        var nivel = document.getElementById('nivel').value;

        // Mostrar los valores seleccionados en un alert
        alert("Materia: " + materia + "\nGrado: " + grado + "\nDestreza: " + destreza + "\nNivel: " + nivel);

        // Aquí podrías hacer una consulta AJAX al backend si lo tienes
    }

    // Asignar la función al botón de búsqueda
    document.querySelector("button").onclick = buscarTarea;
    function showSection(sectionId) {
      const sections = document.querySelectorAll('.section');
      sections.forEach(section => section.classList.add('hidden'));
      document.getElementById(sectionId).classList.remove('hidden');
  }

  function registerUser() {
      alert("Registro exitoso.");
      showSection('login-register');
  }