import axios from 'axios'
import { statusFunctions, logRequestError } from '../utils/utils.js'
import { insertRowIntoTable } from '../utils/volumes-embarque.js'
import { BASE_URL_API } from '../variaveisAmbiente.js'

const form = document.querySelector('#form')

//manipulação de DOM 
//buscando clientes cadastrados
axios.get(`${BASE_URL_API}/clientes`).then(res => {
    // adicionando clientes
    const selectCliente = document.querySelector('#clientes-disponiveis')

    res.data.clientes.forEach(cliente => {
        let option = `
        <option value=${cliente.id}>${cliente.nome}</option>
        `
        if (JSON.parse(localStorage.getItem('cliente-selecionado')) === cliente.id) {
            option = `
            <option value=${cliente.id} selected>${cliente.nome}</option>
            `
        }
        selectCliente.innerHTML += option
    })

})

// colocando a data default igual a data atual!
const date = new Date();

let day = date.getDate();
let month = date.getMonth() + 1;
let year = date.getFullYear();

if (month < 10) month = "0" + month;
if (day < 10) day = "0" + day;

let today = year + "-" + month + "-" + day;
document.getElementById('data').value = today;


// Adicionando elementos na tabela
insertRowIntoTable()


form.addEventListener('reset', function (e) {
    window.location.href = "./listar-clientes.html"
})

form.addEventListener('submit', function (e) {
    e.preventDefault();
    statusFunctions.loadingStatus()
    document.querySelector('.btn-salvar').disabled = true

    const formData = new FormData(form)
    const listaVolumes = []
    let elemento = 1

    do {
        listaVolumes.push({
            largura: parseInt(formData.get(`larg${elemento}`)),
            comprimento: parseInt(formData.get(`comp${elemento}`)),
            altura: parseInt(formData.get(`alt${elemento}`)),
            peso: parseFloat(formData.get(`peso${elemento}`))
        })
        elemento++
    } while (formData.get(`comp${elemento}`))

    const data = {
        id_cliente: parseInt(formData.get('cliente')),
        descricao: formData.get('descricao'),
        data_chegada: formData.get('data'),
        com_nota_fiscal: formData.get('nota-fiscal') == null ? false : true,
        volumes: listaVolumes
    }

    // armazenando o id do cliente para selecioná-lo automáticamente quando a página recarregar
    if (data.id_cliente) {
        localStorage.setItem('cliente-selecionado', data.id_cliente)
    }

    axios.post(`${BASE_URL_API}/embarques`, data)
        .then(res => {
            statusFunctions.sucessStatus("Embarque cadastrado com sucesso!")
        })
        .catch(err => {
            logRequestError(err)
            statusFunctions.failedStatus("Não foi possível cadastrar o embarque!")
        })
        .then(res => {
            setTimeout(() => window.location.href = './cadastro-embarque.html', 5000)
        })

})



