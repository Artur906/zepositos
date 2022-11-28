import './style.css'
import javascriptLogo from './javascript.svg'
import { setupCounter } from './counter.js'

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
    <button id="cadastro" rel="stylesheet">Página de cadastro</button>
  </div>
`
document.querySelector("#cadastro").addEventListener("click", () => {
  document.querySelector('#app').innerHTML = `
  <h1>Cadastro</h1>
  <div>
      <form action="" id="input-up">
          <label for="name">Nome do cliente</label>
          <br>
          <input type="text" id="name">
      </form>
      <form action="" id="input-down">
          <label for="name">Telefone</label>
          <br>
          <input type="text" id="name">
      </form>
      <input type="button" id="btnSalvar" class="btnSalvarGreen" value="SALVAR" onclick="salvarForms()" />
      <input type="button" id="btnCancelar" class="btnSalvarGreen" value="Cancelar" onclick="salvarForms()" />
  </div>
  `
})

setupCounter(document.querySelector('#counter'))
