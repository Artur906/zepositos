// import axios from 'axios'
// import {BASE_URL_API} from '../variaveisAmbiente'

const dados = { clientes: [
    {
        nome: 'maria', 
        quant_embarques: 0,
        id: 1
    },
    {
        nome: 'JOse', 
        quant_embarques: 0,
        id: 2
    },
    {
        nome: 'mGuiador', 
        quant_embarques: 0,
        id: 3
    },
    {
        nome: 'maria4', 
        quant_embarques: 0,
        id: 4
    }
]}
const tabela = document.querySelector('.table-body')

dados.clientes.forEach(cliente => { 
    let table_row = 
        ` 
            <tr id_cliente="${cliente.id}" data-toggle="modal" data-target="#exampleModalCenter">
                <td>${cliente.nome}</td>
                <td>${cliente.quant_embarques}</td>
            </tr> 
        `
    tabela.innerHTML += table_row;
});

const linhas = document.querySelectorAll('.table-body tr')

linhas.forEach(linha => {
    linha.addEventListener('click', () => {
        let idCliente = linha.getAttribute("id_cliente")
        modalEmbarques(idCliente)
    })
})

// vai colocar os elementos na modal
function modalEmbarques(clienteId) {
    const cliente = dados.clientes.find(cliente => {return cliente.id == clienteId})
    document.querySelector('.modal-title').textContent = cliente.nome
    document.querySelector('.modal-body').innerHTML = "aaaaaaaaaaaaaaaaaa eu to vivoooooo"
}

console.log(id)
