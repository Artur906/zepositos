
import axios from 'axios' //node
import { textMarshal } from 'text-marshal' // node
import { BASE_URL_API } from '../variaveisAmbiente.js'


const form = document.querySelector('#form')

form.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(form)

    const data = {
        nome: formData.get('nome'),
        telefone: formData.get('telefone'),
    }

    document.querySelector('#status').innerHTML =
        `<div class="spinner-border" role="status">
            <span class="sr-only"></span>
        </div>`

    axios.post(`${BASE_URL_API}/clientes`, data)
        .then(res => {
            document.querySelector('#status').innerHTML =
                `<div class="alert alert-success" role="alert">
                Cliente Cadastrado!
            </div>`
        })
        .catch(err => {
            document.querySelector('#status').innerHTML =
                `<div class="alert alert-danger" role="alert">
                Não foi possível cadastrar o cliente!
            </div>`
        })
        .then(res => {
            setTimeout(() => window.location.href = "./cadastro-cliente.html", 5000)
        })
})



form.addEventListener('reset', function (e) {
    window.location.href = "../listar-clientes/listar-clientes.html"
})

const cardnumber = document.getElementById('telefone');

cardnumber.oninput = function (e) {
    let data = textMarshal({
        input: e.target.value,
        template: cardnumber.getAttribute('data-pattern'),
        disallowCharacters: [/[a-z]/],
    });

    cardnumber.value = data.marshaltext;
};