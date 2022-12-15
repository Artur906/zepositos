import axios from 'axios'
import { statusFunctions, criarLinha, logRequestError } from './utils.js'
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
const tabela = document.querySelector('.table-body')
let numeroElemento = 0


const adicionandoElementoNaTabela = () => {
    numeroElemento++
    const elementoPai = tabela

    const novaLinha = criarLinha(numeroElemento)
   
    elementoPai.insertBefore(novaLinha, elementoPai.firstChild)

    //mudar o botão dos elementos anteriores para o de remover 
    const botoes = document.querySelectorAll('.add-row')
    mudarBotoes(botoes)
}

function mudarBotoes(botoes) {
    botoes.forEach((botao, index) => {
        if (index > 0) {
            botao.className = 'btn btn-danger rmv-row'
            botao.value = '   '

            botao.removeEventListener('click', adicionandoElementoNaTabela)
            botao.addEventListener('click', e => {
                // o parentElement é o elemento pai, o botão está dentro de um td, que está dentro de um tr
                removerElementoDaTela(botao.parentElement.parentElement)
                reorganizarContagemDeLinhas()
            })
        } else {
            botao.addEventListener('click', adicionandoElementoNaTabela)
        }
    })
}

const removerElementoDaTela = (elemento) => {
    tabela.removeChild(elemento)
}

const reorganizarContagemDeLinhas = () => {
    numeroElemento--
    const linhas = document.querySelectorAll('.linha')
    linhas.forEach((linha, index) => {
        const indexInvertido = linhas.length - index
        //acessando cada um dos elementos da linha
        //contador
        linha.children[0].innerHTML = indexInvertido
        //comp 
        linha.children[1].firstElementChild.setAttribute('name', `comp${indexInvertido}`) 
        //alt 
        linha.children[2].firstElementChild.setAttribute('name', `alt${indexInvertido}`) 
        //larg 
        linha.children[3].firstElementChild.setAttribute('name', `larg${indexInvertido}`) 
        //peso 
        linha.children[4].firstElementChild.setAttribute('name', `peso${indexInvertido}`) 
    })
}

adicionandoElementoNaTabela()


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



