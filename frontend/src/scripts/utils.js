
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