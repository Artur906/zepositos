import axios from 'axios'
import { statusFunctions } from './utils.js'
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


const updateNotaFiscalCheckBox = (bool) =>{
    document.getElementById('flexCheckDefault').checked = bool
    const formData = new FormData(form)
    formData.set('nota-fiscal', bool)
}   







const id_embarque = params.id
console.log(id_embarque)


let embarque = await pegarEmbarque(id_embarque)
let volumes_embarque = await pegarVolumesEmbarque(id_embarque)

console.log(embarque)
console.log(volumes_embarque)


const form = document.querySelector('#form')
updateNotaFiscalCheckBox(embarque.com_nota_fiscal)
document.getElementById("descricao").value = embarque.descricao
document.getElementById("data").value = embarque.data_chegada


// quando o botao salvar é clicado:
form.addEventListener('submit', function (e) {
    e.preventDefault();
    statusFunctions.loadingStatus()
    document.querySelector('.btn-salvar').disabled = true
    
    const formData = new FormData(form)
    const data = {
        descricao: formData.get('descricao'),
        data_chegada: formData.get('data'),
        com_nota_fiscal: formData.get('nota-fiscal') == null ? false : true
    }
    axios.patch(`${BASE_URL_API}/embarques/${id_embarque}`, data)
        .then(res=>{
            statusFunctions.sucessStatus("Embarque Atualizado com sucesso!")
        })
        .except(err=>{
            statusFunctions.failedStatus("Não foi possível atualizar o embarque!")
        })
    
})