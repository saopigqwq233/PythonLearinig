import pprint

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment
"""example_xlsx = load_workbook('example.xlsx')
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

for columnsofsheet1 in list(Sheet1_example_xlsx.columns):
    for cellobj in columnsofsheet1:
        print(cellobj.coordinate, cellobj.value)
    print('---EOF---OF---COLUMN---')"""
# 人口普查.xlsx
wb = load_workbook('censuspopdata.xlsx')
ws = wb.active
countryData = {}
for row in range(2, ws.max_row+1):
    state = ws.cell(row=row, column=2).value
    country = ws.cell(row=row, column=3).value
    pop = ws.cell(row=row, column=4).value

    countryData.setdefault(state, {})
    countryData[state].setdefault(country, {'tracts': 0, 'pop': 0})
    countryData[state][country]['tracts'] += 1
    countryData[state][country]['pop'] += int(pop)

print('Writing results...')
resultFile = open('census2010.py','w')
resultFile.write('allData = '+pprint.pformat(countryData))
resultFile.close()
print('Done.')
outbook = Workbook()
outsheet = outbook.active
outsheet.title = 'Summery'
outsheet.cell(row=1, column=1).value = '州名'
outsheet.cell(row=1, column=2).value = '县名'
outsheet.cell(row=1, column=3).value = '普查区数量'
outsheet.cell(row=1, column=4).value = '人口总数'

row_in_out = 2
ws.merge_cells('E1:E2')
for state in countryData:
    outsheet.merge_cells(start_row=row_in_out, start_column=1, end_row=len(countryData[state])+row_in_out-1, end_column=1)
    outsheet.cell(row=row_in_out, column=1).value = state
    for country in countryData[state]:
        outsheet.cell(row=row_in_out, column=2).value = country
        outsheet.cell(row=row_in_out, column=3).value = countryData[state][country]['tracts']
        outsheet.cell(row=row_in_out, column=4).value = countryData[state][country]['pop']
        row_in_out += 1

for row in list(outsheet.rows):
    for cellofrow in row:
        cellofrow.alignment = Alignment(horizontal='center', vertical='center')

outbook.save('output.xlsx')
