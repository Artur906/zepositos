import axios from 'axios'
import { statusFunctions, criarLinha } from './utils.js'
import { BASE_URL_API } from '../variaveisAmbiente.js'


// pegar parametros inseridos na URL
const params = new Proxy(new URLSearchParams(window.location.search), {
    get: (searchParams, prop) => searchParams.get(prop),
});


//requisições
async function pegarEmbarque(id) {
    return (await axios.get(`${BASE_URL_API}/embarques/${id_embarque}`)).data
}
async function pegarVolumesEmbarque(id_embarque) {
    return (await axios.get(`${BASE_URL_API}/embarques/${id_embarque}/volumes`)).data
}
async function pegarClienteDonoDoEmbarque(id_cliente) {
    if(id_cliente) {
        return (await axios.get(`${BASE_URL_API}/clientes/${id_cliente}`)).data
    }
    return null
}


const updateNotaFiscalCheckBox = (bool) => {
    document.getElementById('flexCheckDefault').checked = bool
    const formData = new FormData(form)
    formData.set('nota-fiscal', bool)
}


const id_embarque = params.id
console.log(id_embarque)


let embarque = await pegarEmbarque(id_embarque)
let volumes_embarque = await pegarVolumesEmbarque(id_embarque)
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
updateNotaFiscalCheckBox(embarque.com_nota_fiscal)
document.getElementById("descricao").value = embarque.descricao
document.getElementById("data").value = embarque.data_chegada

volumes_embarque.volumes.forEach((volume, index) => {
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

    tabela.append(novaLinha)
})

// quando o botao salvar é clicado:
form.addEventListener('submit', function (e) {
    e.preventDefault();
    statusFunctions.loadingStatus()
    document.querySelector('.btn-salvar').disabled = true

    const formData = new FormData(form)
    const data = {
        id_cliente: formData.get('cliente'), 
        descricao: formData.get('descricao'),
        data_chegada: formData.get('data'),
        com_nota_fiscal: formData.get('nota-fiscal') == null ? false : true
    }
    axios.patch(`${BASE_URL_API}/embarques/${id_embarque}`, data)
        .then(res => {
            statusFunctions.sucessStatus("Embarque Atualizado com sucesso!")
        })
        .catch(err => {
            console.log(err)
            statusFunctions.failedStatus("Não foi possível atualizar o embarque!")
        })

})



