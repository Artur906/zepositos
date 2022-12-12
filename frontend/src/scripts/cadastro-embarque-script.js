import axios from 'axios'
import { statusFunctions } from './utils.js'
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

    const linha =
        `
    <td> 
        ${numeroElemento}
    </td> 
    <td>
        <input class="form-control" type="text" name="comp${numeroElemento}"  placeholder="Cm" required>
    </td>
    <td>
        <input type="text" class="form-control" name="alt${numeroElemento}" placeholder="Cm" required>
    </td>
    <td>
        <input type="text" class="form-control" name="larg${numeroElemento}"  placeholder="Cm" required>
    </td>
    <td>
        <input type="text" class="form-control" name="peso${numeroElemento}"  placeholder="Kg" required>
    </td>
    <td>
        <input 
                type="button"
                class="btn btn-primary add-row" 
                value="   "
            />
    </td>
`

    const novaLinha = document.createElement('tr')
    novaLinha.className = 'linha'
    novaLinha.innerHTML = linha
    elementoPai.insertBefore(novaLinha, elementoPai.firstChild)

    //mudar o botão dos elementos anteriores para o de remover 
    const botoes = document.querySelectorAll('.add-row')
    return mudarBotoes(botoes)


}


function mudarBotoes(botoes) {
    botoes.forEach((botao, index) => {
        if (index > 0) {
            botao.className = 'btn btn-danger rmv-row'
            botao.value = '   '

            botao.removeEventListener('click', adicionandoElementoNaTabela)
            botao.addEventListener('click', e => {
                removerElementoDaTela(botao.parentElement.parentElement)
            })
        } else {
            botao.addEventListener('click', adicionandoElementoNaTabela)
        }
    })
}

const removerElementoDaTela = (elemento) => {
    tabela.removeChild(elemento)
}

adicionandoElementoNaTabela()


form.addEventListener('reset', function (e) {
    window.location.href = "./listar-clientes.html"
})

form.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(form)

    document.querySelector('.btn-salvar').disabled = true

    document.querySelector('#status').innerHTML =
        `<div class="spinner-border" role="status">
            <span class="sr-only"></span>
        </div>`

    const data = {
        id_cliente: parseInt(formData.get('cliente')),
        descricao: formData.get('descricao'),
        data_chegada: formData.get('data'),
        com_nota_fiscal: formData.get('nota-fiscal') == null ? false : true
    }

    // armazenando o id do cliente para selecioná-lo automáticamente quando a página recarregar
    if (data.id_cliente) {
        localStorage.setItem('cliente-selecionado', data.id_cliente)
    }

    axios.post(`${BASE_URL_API}/embarques`, data)
        .then(res => {
            const volumes = []
            let elemento = 1

            do {
                volumes.push({
                    id_embarque: res.data.id,
                    largura: parseInt(formData.get(`larg${elemento}`)),
                    comprimento: parseInt(formData.get(`comp${elemento}`)),
                    altura: parseInt(formData.get(`alt${elemento}`)),
                    peso: parseFloat(formData.get(`peso${elemento}`))
                })
                elemento++
            } while (formData.get(`comp${elemento}`))

            volumes.forEach(volume => {
                axios.post(`${BASE_URL_API}/volumes`, volume)
                    .catch(err => {
                        statusFunctions.failedStatus("Não foi possível cadastrar o embarque (erro no volume)!")
                        console.log(err.response.data)
                        return
                    })
            })

            statusFunctions.sucessStatus("Embarque cadastrado com sucesso!")
        })
        .catch(err => {
            statusFunctions.failedStatus("Não foi possível cadastrar o embarque!")
            console.log(err.response.data.message)
        })
        .then(res => {
            setTimeout(() => window.location.href = './cadastro-embarque.html', 5000)
        })

})


