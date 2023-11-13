const table = document.getElementById('table');
const transposeButton = document.getElementById('transpose');
const addRowButton = document.getElementById('addRow');
const addColumnButton = document.getElementById('addColumn');
let restricted = false;

function createTable(size) {
    // clean the table
    while (table.hasChildNodes()) {
        table.removeChild(table.lastChild);
    }

    for (let i = 0; i < size; i++) {
        const row = document.createElement('tr');
        for (let j = 0; j < size; j++) {
            const cell = document.createElement('td');
            cell.textContent = Math.floor(Math.random() * 100);
            cell.addEventListener('click', toggleCellSelection);
            row.appendChild(cell);
        }
        table.appendChild(row);
    }

    // These lines must be after the creation of the buttons
    transposeButton.addEventListener('click', transposeTable);
    addRowButton.addEventListener('click', addRow);
    addColumnButton.addEventListener('click', addColumn);
}

let maxSelections = [];

document.getElementById('updateMaxSelection').addEventListener('click', function () {
    const maxSelectionInput = document.getElementById('maxSelection');
    const newValue = parseInt(maxSelectionInput.value);
    if (!isNaN(newValue) && newValue >= 0) {
        restricted = true;
        maxSelections = Array.from({ length: table.rows.length }, () => newValue);
    } else {
        alert('Please enter a valid non-negative number for max selection.');
    }
});

function toggleCellSelection(event) {
    const cell = event.target;
    const isSelected = cell.classList.contains('selected');
    const rowIndex = cell.parentElement.rowIndex;

    if (isSelected) {
        cell.classList.remove('selected', 'selected-even', 'selected-odd');
    } else {
        if (canSelectCell(cell, rowIndex)) {
            cell.classList.add('selected');
            if (parseInt(cell.textContent) % 2 === 0) {
                cell.classList.add('selected-even');
            } else {
                cell.classList.add('selected-odd');
            }
        }
    }
}

function canSelectCell(cell, rowIndex) {
    if (!restricted) {
        return true;
    }
    if (rowIndex < 0 || rowIndex >= maxSelections.length) {
        return false;
    }

    const maxSelection = maxSelections[rowIndex];
    const selectedCells = Array.from(cell.parentElement.cells).filter(
        (cell) => cell.classList.contains('selected')
    );

    if (selectedCells.length >= maxSelection) {
        return false;
    }

    const cellIndex = cell.cellIndex;
    const leftCell = cellIndex > 0 ? cell.parentElement.cells[cellIndex - 1] : null;
    const rightCell =
        cellIndex < cell.parentElement.cells.length - 1
            ? cell.parentElement.cells[cellIndex + 1]
            : null;

    return !(
        (leftCell && leftCell.classList.contains('selected')) ||
        (rightCell && rightCell.classList.contains('selected')
        )
    );
}

function transposeTable() {
    const rows = Array.from(table.rows);
    const numRows = rows.length;
    const numCols = rows[0].cells.length;
    const newTable = new Array(numCols).fill(null).map(() => []);

    for (let i = 0; i < numRows; i++) {
        for (let j = 0; j < numCols; j++) {
            newTable[j][i] = rows[i].cells[j].textContent;
        }
    }

    while (table.rows.length > 0) {
        table.deleteRow(0);
    }

    for (let i = 0; i < numCols; i++) {
        const newRow = table.insertRow(i);
        for (let j = 0; j < numRows; j++) {
            const cell = newRow.insertCell(j);
            cell.textContent = newTable[i][j];
            cell.addEventListener('click', toggleCellSelection);
        }
    }
}

function addRow() {
    const newRow = document.createElement('tr');
    const cols = table.rows[0].cells.length;
    for (let j = 0; j < cols; j++) {
        const cell = document.createElement('td');
        cell.textContent = Math.floor(Math.random() * 100);
        cell.addEventListener('click', toggleCellSelection);
        newRow.appendChild(cell);
    }
    table.appendChild(newRow);
}

function addColumn() {
    const rows = table.rows;
    for (let i = 0; i < rows.length; i++) {
        const cell = document.createElement('td');
        cell.textContent = Math.floor(Math.random() * 100);
        cell.addEventListener('click', toggleCellSelection);
        rows[i].appendChild(cell);
    }
}

document.getElementById('createTable').addEventListener('click', function () {
    const tableSizeInput = document.getElementById('tableSize');
    const size = parseInt(tableSizeInput.value);
    if (isNaN(size) || size < 1){
        alert('Please Enter a valid size for the Table');
        return;
    }
    createTable(size);
});


