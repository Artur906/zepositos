
export const statusFunctions = {
   elementoStatus: document.querySelector('#status'), 
   loadingStatus: () => {
       statusFunctions.elementoStatus.innerHTML =
           `<div class="spinner-border" role="status">
            <span class="sr-only"></span>
           </div>`
   },
   sucessStatus: text => {
       statusFunctions.elementoStatus.innerHTML =
           `<div class="alert alert-success" role="alert">
               ${text ? text : "Cliente Cadastrado!"}
           </div>`
   }, 
   failedStatus: text => {
       statusFunctions.elementoStatus.innerHTML =
           `<div class="alert alert-danger" role="alert">
               ${text ? text : "Não foi possível cadastrar o cliente!"}
           </div>`
   }
}

export const criarLinha = (numeroElemento) => {

    const linha =
        `
    <td> 
    ${numeroElemento}
    </td> 
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
    <td>
    <input 
            type="button"
            class="btn btn-primary add-row" 
            value="   "
        />
    </td>
    `

    const novaLinha = document.createElement('tr')
    novaLinha.className = 'linha'
    novaLinha.innerHTML = linha

    return novaLinha
}

export const logRequestError = (err) => {
    console.log(err.response.data.errors)
    console.log(err.response.data.message)
}