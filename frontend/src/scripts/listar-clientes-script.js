import axios from 'axios'
import { BASE_URL_API } from '../variaveisAmbiente'

const tabelaClientes = document.querySelector('.table-clientes')


//requisições
async function pegarClientes() {
    const clientes = (await axios.get(`${BASE_URL_API}/clientes`)).data

    return clientes
}

async function pegarEmbarquesCliente(idCliente) {
    const embarques = (await axios.get(`${BASE_URL_API}/clientes/${idCliente}/embarques`)).data
    return embarques
}

async function pegarEmbarquesAtivosCliente(idCliente) {

    const response =  (await axios.get(`${BASE_URL_API}/clientes/${idCliente}/embarques`)).data
    let embarquesAtivos = []
    response.embarques.forEach(emb => {
        if(!(emb["embarcado"])){
            embarquesAtivos.push(emb)
        }
    })
    return embarquesAtivos
}


let dadosClientes = await pegarClientes()

dadosClientes.clientes.forEach(cliente => {
    let table_row =
        ` 
            <tr id_cliente="${cliente.id}" data-toggle="modal" data-target="#exampleModalCenter" class="tr-hover">
                <td>${cliente.nome}</td>
                <td>${cliente.quant_embarques_ativos}</td>
            </tr> 
        `
    tabelaClientes.innerHTML += table_row;
});

const linhasTableClientes = document.querySelectorAll('.table-clientes tr')

linhasTableClientes.forEach(linha => {
    linha.addEventListener('click', () => {
        let idCliente = linha.getAttribute("id_cliente")
        const cliente = dadosClientes.clientes.find(cliente => { return cliente.id == idCliente })
        modalEmbarques(cliente)
    })
})


// vai colocar os elementos na modal
async function modalEmbarques(cliente) {
    document.querySelector('.modal-title').textContent = `Embarques Ativos de ${cliente.nome}`
    const tabelaEmbarques = document.querySelector('.table-embarques')
    tabelaEmbarques.innerHTML = ''

    const embarquesAtivos = await pegarEmbarquesAtivosCliente(cliente.id)
    
    embarquesAtivos.forEach(embarque => {
        const statusEmbarque = () => {
            if(embarque.embarcado){
                return `<td class="embarcado" itle="Embarcado"></td>`
            }
            if(embarque.pago) {
                return `<td class="pago" title="Pago"></td>`
            }
            if(embarque.registrado) {
                return `<td class="registrado" title="Registrado"></td>`
            }
            if(embarque.com_nota_fiscal){
                return `<td class="nota-fiscal" title="Possui nota fiscal"></td>`
            } 
                return `<td class="sem-status" title="Não possui nota fiscal"></td>`
        }
        let table_row =
            ` 
                <tr class="${embarque.urgente ? 'table-primary bg-color-green' : ''} tr-hover" embarque_id = "${embarque.id}" onclick='location.href="embarque.html?id=${embarque.id}"' >
                    ${statusEmbarque()}
                    <td>${embarque.descricao}</td>
                    <td>${embarque.quant_volumes}</td>
                    <td>${embarque.peso_total}</td>
                    <td>${embarque.com_nota_fiscal ? "sim" : "não"}</td>
                    <td>${embarque.data_chegada}</td>
                </tr>
            `
            
        tabelaEmbarques.innerHTML += table_row;
    });

    const linhasTabelaEmbarques = document.querySelectorAll('.table-embarques tr')
}