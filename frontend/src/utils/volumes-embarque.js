const rowFactory = (elementIndex) => {

  const row =
      `
  <td> 
      ${elementIndex}
  </td> 
  <td>
      <input class="form-control" type="text" name="comp${elementIndex}"  placeholder="Cm" required>
  </td>
  <td>
      <input type="text" class="form-control" name="alt${elementIndex}" placeholder="Cm" required>
  </td>
  <td>
      <input type="text" class="form-control" name="larg${elementIndex}"  placeholder="Cm" required>
  </td>
  <td>
      <input type="text" class="form-control" name="peso${elementIndex}"  placeholder="Kg" required>
  </td>
  <td>
  <input 
          type="button"
          class="btn btn-primary btn-add-row" 
          value="   "
      />
  </td>
  `

  const newRow = document.createElement('tr')
  newRow.className = 'table-row'
  newRow.innerHTML = row

  return newRow
}

export const insertRowIntoTable = (callback, volume) => {
  const table = document.querySelector('.table-body')
  let countOfRows = document.querySelectorAll('.table-row').length

  const newRow = rowFactory(++countOfRows)

  if(volume) {
    console.log(callback)
    callback(newRow, volume)
  }

  table.insertBefore(newRow, table.firstChild)

  //mudar o botão dos elementos anteriores para o de remover 
  const buttons = document.querySelectorAll('.btn-add-row')
  changeButton(buttons)
}

const changeButton = (buttons) => {
  buttons.forEach((button, index) => {
      if (index > 0) {
          button.className = 'btn btn-danger btn-rmv-row'
          button.value = '   '

          button.removeEventListener('click', insertRowIntoTable)
          button.addEventListener('click', e => {
              // o parentElement é o elemento pai, o botão está dentro de um td, que está dentro de um tr
              removeRowFromTable(button.parentElement.parentElement)
          })

      } else {
          button.addEventListener('click', insertRowIntoTable)
      }
  })
}

const removeRowFromTable = (row) => {
  const table = document.querySelector('.table-body')
  table.removeChild(row)
  replaceRowsIndex()
}

const replaceRowsIndex = () => {
  const rows = document.querySelectorAll('.table-row')
  rows.forEach((row, index) => {
      const upSideDownIndex = rows.length - index
      //acessando cada um dos elementos da linha
      //contador
      row.children[0].innerHTML = upSideDownIndex
      //comp 
      row.children[1].firstElementChild.setAttribute('name', `comp${upSideDownIndex}`)
      //alt 
      row.children[2].firstElementChild.setAttribute('name', `alt${upSideDownIndex}`)
      //larg 
      row.children[3].firstElementChild.setAttribute('name', `larg${upSideDownIndex}`)
      //peso 
      row.children[4].firstElementChild.setAttribute('name', `peso${upSideDownIndex}`)
  })
}

export const addDataToRow = (row, volume) => {
  const index = document.querySelectorAll('.table-row').length
  //acessando cada um dos elementos da linha
  //contador
  row.children[0].value = index + 1
  //comp 
  row.children[1].firstElementChild.value = volume.comprimento
  //alt 
  row.children[2].firstElementChild.value = volume.altura
  //larg 
  row.children[3].firstElementChild.value = volume.largura
  //peso 
  row.children[4].firstElementChild.value = volume.peso
}