'''

Public API:
// Reads the value of the cell after formula calculations
getCell(cell: String): Int

// Sets the value of the cell
setCell(cell: String, value: String): void

// Triggers when the value of a cell updates
onCellChange(cell: String, callback: (newValue: Int, cell: String) => void): void


Valid Cell Values
Single Number
= 1

Formula Addition
= 1 + 2

Cell Reference Addition
= A1 + A2 + 2

Additional constraints:
- Only addition operator
- Assume perfect input (single space delimited operands and operators)
- No circular references between cells
- Function not allowed to reference unset cells

setCell("A1", "= 2");
getCell("A1"); // returns 2

setCell("A2", "= 1 + 2")
getCell("A2") // return 3

setCell("B1", "= A1 + A2 + 1")
getCell("B1") // return 6

onCellChange("A1", (newValue, cell) => {
  console.log("New value:", cell, newValue)
  // New value: A1, 1
})
onCellChange("B1", (newValue, cell) => {
  console.log("New value:", cell, newValue)
  // New value: B1, 5
})
setCell("A1", "= 1") 

'''
