import axios from 'axios'
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
        if(JSON.parse(localStorage.getItem('cliente-selecionado')) === cliente.id){
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
let numeroElemento = 1

document.querySelector('.add-row').addEventListener('click', e => {
    e.preventDefault()
    numeroElemento++

    const novaLinha =
        `
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
    
    `
    const novoElemento = document.createElement('tr')
    novoElemento.className = 'linha'
    novoElemento.innerHTML = novaLinha

    tabela.append(novoElemento)


    
})

form.addEventListener('reset', function (e) {
    window.location.href = "../listar-clientes/listar-clientes.html"
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
    localStorage.setItem('cliente-selecionado', data.id_cliente)

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
                    document.querySelector('#status').innerHTML =
                        `<div class="alert alert-danger" role="alert">
                            Não foi possível cadastrar o embarque (erro no volume)!
                        </div>`
                    console.log(err.response.data)
                    return
                })
            })

            document.querySelector('#status').innerHTML =
                `<div class="alert alert-success" role="alert">
                    Embarque cadastrado com sucesso!
                </div>`
        })
        .catch(err => {
            document.querySelector('#status').innerHTML =
                `<div class="alert alert-danger" role="alert">
                    Não foi possível cadastrar o embarque!
                </div>`
            console.log(err.response.data.message)
        })
        /*.then(res => {
            setTimeout(() => window.location.href = './cadastro-embarque.html', 5000)
        })*/

})



