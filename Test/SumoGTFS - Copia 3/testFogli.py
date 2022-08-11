import gspread

sa = gspread.service_account()
sh = sa.open("Test SUMO")

wks = sh.worksheet("Foglio1")

print('Rows:', wks.row_count)
print('Cols:', wks.col_count)

print(wks.acell('A2').value)
wks.update('A3', 'Lista di parametri da aggiungere')