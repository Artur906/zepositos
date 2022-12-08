// import axios from 'axios'
// import {BASE_URL_API} from '../variaveisAmbiente'

function modalEmbarques(clienteId) {
    console.log("aaaaaaaaaaaaaaaaaa eu to vivoooooo")
}

const dados = { clientes: [
    {
        nome: 'maria', 
        quant_embarques: 0,
        id: 1
    },
    {
        nome: 'maria2', 
        quant_embarques: 0,
        id: 2
    },
    {
        nome: 'maria3', 
        quant_embarques: 0,
        id: 3
    },
    {
        nome: 'maria4', 
        quant_embarques: 0,
        id: 4
    }
]}
const tabela = document.querySelector(".table-body")

dados.clientes.forEach(cliente => { 
    let table_row = 
        ` 
            <tr onclick = "modalEmbarques()">
                <td>${cliente.nome}</td>
                <td>${cliente.quant_embarques}</td>
            </tr> 
        `
    tabela.innerHTML += table_row;
});

