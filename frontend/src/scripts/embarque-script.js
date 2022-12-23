import axios from 'axios'
import { statusFunctions, logRequestError } from '../utils/utils.js'
import { insertRowIntoTable, addDataToRow } from '../utils/volumes-embarque.js';
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

document.getElementById('notaFiscalCheckBox').checked = embarque.com_nota_fiscal
document.getElementById('registradoCheckBox').checked = embarque.registrado
document.getElementById('pagoCheckBox').checked = embarque.pago
document.getElementById('embarcadoCheckBox').checked = embarque.embarcado
document.getElementById('urgenteCheckBox').checked = embarque.urgente

document.getElementById("descricao").value = embarque.descricao
document.getElementById("data").value = embarque.data_chegada

// inserindo os volumes na table
embarque.volumes.forEach((volume) => {
    insertRowIntoTable(addDataToRow, volume)
})

// quando o botao salvar é clicado:
form.addEventListener('submit', function (e) {
    e.preventDefault()
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

const fieldset = document.querySelector('fieldset')
const btnEditar = document.querySelector('#editar')

const btnSalvar = document.querySelector('.btn-salvar')
const btnCancelar = document.querySelector('#cancelar')
const btnDeletar = document.querySelector('#bttn-deletar')

// sumindo com os botões 
btnSalvar.style.display = "none"
btnCancelar.style.display = "none"
btnDeletar.style.display = "none"

// quando o botão editar é clicado
btnEditar.addEventListener('click', function (e) {
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

