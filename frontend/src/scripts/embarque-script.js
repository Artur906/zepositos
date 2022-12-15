import axios from 'axios'
import { statusFunctions, criarLinha, logRequestError } from './utils.js'
import { BASE_URL_API } from '../variaveisAmbiente.js'


// pegar parametros inseridos na URL
const params = new Proxy(new URLSearchParams(window.location.search), {
    get: (searchParams, prop) => searchParams.get(prop),
});


//requisições
async function pegarEmbarque(id) {
    return (await axios.get(`${BASE_URL_API}/embarques/${id}`)).data
}
async function pegarClienteDonoDoEmbarque(id_cliente) {
    if (id_cliente) {
        return (await axios.get(`${BASE_URL_API}/clientes/${id_cliente}`)).data
    }
    return null
}

async function deletarEmbarque(id_embarque) {
    return (await axios.delete(`${BASE_URL_API}/embarques/${id}`)).data
}

/*
function updateCheckBoxElement(bool, elementId){
    document.getElementById('elementId').checked = bool
    let formData = new FormData(form)
    formData.set('registrado', bool)
}*/

function updateRegistradoCheckBox(bool) {
    document.getElementById('registradoCheckBox').checked = bool
}


const id_embarque = params.id

let embarque = await pegarEmbarque(id_embarque)
let cliente = await pegarClienteDonoDoEmbarque(embarque.id_cliente)

const clienteSelecionado = document.querySelector('#clientes-disponiveis')

if (cliente) {
    let option = `
    <option value=${cliente.id} selected>${cliente.nome}</option>
    `
    clienteSelecionado.innerHTML = option
} else {

    axios.get(`${BASE_URL_API}/clientes`).then(res => {
        // adicionando clientes
        res.data.clientes.forEach(cliente => {
            let option = `
            <option value=${cliente.id}>${cliente.nome}</option>
            `
            clienteSelecionado.innerHTML += option
        })
    })
}

const form = document.querySelector('#form')
const tabela = document.querySelector(".table-body")

document.getElementById('notaFiscalCheckBox').checked = embarque.com_nota_fiscal
document.getElementById('registradoCheckBox').checked = embarque.registrado
document.getElementById('pagoCheckBox').checked = embarque.pago
document.getElementById('embarcadoCheckBox').checked = embarque.embarcado
document.getElementById('urgenteCheckBox').checked = embarque.urgente

document.getElementById("descricao").value = embarque.descricao
document.getElementById("data").value = embarque.data_chegada

/*
 FUNÇÕES NESCESSÁRIAS PARA EDIÇÃO DE VOLUMES 
 ------------ ---------- ------------- -------  
 porque elas estão aqui? 
 porque eu tive dificuldade em fazer elas funciorem por meio de importação 
 elas acessam a variável numero elemento para fazer a organização dos volumes 
 */
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
//fim funções nescessárias para edição de volumes


embarque.volumes.forEach((volume, index) => {
    numeroElemento++
    const novaLinha = criarLinha(index + 1)

    //acessando cada um dos elementos da linha
    //contador
    novaLinha.children[0].value = index + 1
    //comp 
    novaLinha.children[1].firstElementChild.value = volume.comprimento
    //alt 
    novaLinha.children[2].firstElementChild.value = volume.altura
    //larg 
    novaLinha.children[3].firstElementChild.value = volume.largura
    //peso 
    novaLinha.children[4].firstElementChild.value = volume.peso

    tabela.insertBefore(novaLinha, tabela.firstChild)

    //mudar o botão dos elementos anteriores para o de remover 
    const botoes = document.querySelectorAll('.add-row')
    mudarBotoes(botoes)
})

// quando o botao salvar é clicado:
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
        registrado: formData.get('registrado') == null ? false : true,
        pago: formData.get('pago') == null ? false : true,
        embarcado: formData.get('embarcado') == null ? false : true,
        urgente: formData.get('urgente') == null ? false : true,
        volumes: listaVolumes
    }
    axios.patch(`${BASE_URL_API}/embarques/${id_embarque}`, data)
        .then(res => {
            statusFunctions.sucessStatus("Embarque Atualizado com sucesso!")
        })
        .catch(err => {
            logRequestError(err)
            statusFunctions.failedStatus("Não foi possível atualizar o embarque!")
        })
        .then(() => {
            setTimeout(() => window.location.href = './listar-clientes.html', 5000)
        })

})

document.querySelector('.btn-salvar').style.display = "none"
document.querySelector('#cancelar').style.display = "none"
document.querySelector('#bttn-deletar').style.display = "none"
// quando o botão editar é clicado
const botaoEditar = document.querySelector('#editar')

botaoEditar.addEventListener('click', function (e) {
    const fieldset = document.querySelector('fieldset')
    const btnSalvar = document.querySelector('.btn-salvar')
    const btnCancelar = document.querySelector('#cancelar')
    const btnDeletar = document.querySelector('#bttn-deletar')

    btnSalvar.style.display = !fieldset.disabled ? "none" : "inherit"
    btnCancelar.style.display = !fieldset.disabled ? "none" : "inherit"
    btnDeletar.style.display = !fieldset.disabled ? "none" : "inherit"
    fieldset.disabled = !fieldset.disabled
})

const botaoVoltar = document.querySelector('#voltar')
botaoVoltar.addEventListener('click', () => {
    window.location.href = './listar-clientes.html'
})

const modalBtnConfirmDeletion = document.getElementById('modal-btn-confirm-deletion')
modalBtnConfirmDeletion.addEventListener("click", () => {

    //deletarEmbarque(id_embarque)
    axios.delete(`${BASE_URL_API}/embarques/${id_embarque}`, data)
        .then(res => {
            setTimeout(() => window.location.href = "./listar-clientes.html", 500)
        })
        .catch(err => {
            logRequestError(err)
            statusFunctions.failedStatus()
        })

})

