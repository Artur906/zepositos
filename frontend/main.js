import './style.css'
import javascriptLogo from './javascript.svg'
import { setupCounter } from './counter.js'
import axios from 'axios'
import { BASE_URL_API } from './variaveisAmbiente'


document.querySelector('#app').innerHTML = `
  <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
      <img src="${javascriptLogo}" class="logo vanilla" alt="JavaScript logo" />
    </a>
    <h1>Hello Vite!</h1>
    <div class="card">
      <button id="counter" type="button"></button>
    </div>
    <p class="read-the-docs">
      Click on the Vite logo to learn more
    </p>
    <button id="cadastro">Página de cadastro</button>
    <button id="req">Requisição com axios</button>
    
  </div>
`
document.querySelector('#cadastro').addEventListener('click', e => {
  
  document.querySelector('#app').innerHTML = `
  <h1>Cadastro</h1>
  <div>
      <form>
          <label for="nome">Nome do cliente</label>
          <br>
          <input type="text" name="nome" required />
          <br>
          <label for="telefone">Telefone</label>
          <br>
          <input type="text" name="telefone" required />
          <br>
          <input type="submit" id="btnSalvar" class="btnSalvarGreen" value="SALVAR" />
          <input type="button" id="btnCancelar" class="btnSalvarGreen" value="Cancelar" />
      </form>
  </div>
  `
  document.querySelector('#btnSalvar').addEventListener('click', e => {
    e.preventDefault()
  
    const form = document.querySelector('form')
    salvarForms(form)
  })

})


const salvarForms = (form) => {
  const formData = new FormData(form) 

  const dados = {
    "nome": formData.get('nome'),
    "telefone": formData.get('telefone')
  }

  console.log(dados)

  axios.post(`${BASE_URL_API}/clientes`, dados)
    .then(response => console.log(response.data))
}

document.querySelector('#req').addEventListener('click', () => {
  axios.get(`${BASE_URL_API}/clientes`)
    .then(response => {
      console.log(response.data)
    })
})



setupCounter(document.querySelector('#counter'))
