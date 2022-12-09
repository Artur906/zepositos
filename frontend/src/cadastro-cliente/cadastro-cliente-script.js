import axios from 'axios' //node
import { textMarshal } from 'text-marshal' // node
import { BASE_URL_API } from '../variaveisAmbiente.js'

const form = document.querySelector('#form')

//objeto que possui funções que atualizam a DOM do status
const statusFunctions = {
    elementoStatus: document.querySelector('#status'), 
    loadingStatus: () => {
        statusFunctions.elementoStatus.innerHTML =
            `<div class="spinner-border" role="status">
             <span class="sr-only"></span>
            </div>`
    },
    sucessStatus: text => {
        statusFunctions.elementoStatus.innerHTML =
            `<div class="alert alert-success" role="alert">
                ${text ? text : "Cliente Cadastrado!"}
            </div>`
    }, 
    failedStatus: text => {
        statusFunctions.elementoStatus.innerHTML =
            `<div class="alert alert-danger" role="alert">
                ${text ? text : "Não foi possível cadastrar o cliente!"}
            </div>`
    }
}

form.addEventListener('submit', function (e) {
    e.preventDefault()
    statusFunctions.loadingStatus() 
    document.querySelector('.btn-salvar').disabled = true

    const formData = new FormData(form)
    const data = {
        nome: formData.get('nome'),
        telefone: formData.get('telefone'),
    }

    axios.post(`${BASE_URL_API}/clientes`, data)
        .then(res => {
            statusFunctions.sucessStatus()
        })
        .catch(err => {
            statusFunctions.failedStatus()
        })
        .then(res => {
            setTimeout(() => window.location.href = "./cadastro-cliente.html", 5000)
        })
})

form.addEventListener('reset', function (e) {
    window.location.href = "../listar-clientes/listar-clientes.html"
})

//usando regex para padronizar o telefone
const cardnumber = document.getElementById('telefone');

cardnumber.oninput = function (e) {
    let data = textMarshal({
        input: e.target.value,
        template: cardnumber.getAttribute('data-pattern'),
        disallowCharacters: [/[a-z]/],
    });

    cardnumber.value = data.marshaltext;
};