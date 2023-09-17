from openpyxl import Workbook, load_workbook
example_xlsx = load_workbook('example.xlsx')
Sheet1_example_xlsx = example_xlsx['Sheet1']
# for i in range(1, 8):
#   print(i, Sheet1_example_xlsx.cell(row=i, column=2).value)

for i in range(1, Sheet1_example_xlsx.max_row+1):
    print(i, ' ', end='')
    for j in range(1, Sheet1_example_xlsx.max_column+1):
        print(Sheet1_example_xlsx.cell(row=i, column=j).value, ' ', end='')
    print()

for rowofcellobj in Sheet1_example_xlsx['A1':'C7']:
    for cellobj in rowofcellobj:
        print(cellobj.coordinate, cellobj.value)
    print('---EOF---OF---ROW---')
