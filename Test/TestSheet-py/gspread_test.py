import gspread
import pandas
import webbrowser


def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

def updateSheetOLD(busList, worksheet):
    line = 2
    for element in busList:
    #print(element[0])
        for key, value in element[1].items():
            range = "C" + str(line) + ":D" + str(line)
            worksheet.format(range, {
                "horizontalAlignment": "CENTER"
            })
            #Bus Principale Col 1
            worksheet.update_cell(line, 1, element[0])
            #Bus Incontrato Col 2
            worksheet.update_cell(line, 2, key)
            #Tempo Connesso Col 3
            worksheet.update_cell(line, 3, value[0])
            #Orario d'incontro Col 4
            worksheet.update_cell(line, 4, value[1])
            print(element[0] + "  ", end="")
            print(key + " - " + str(value))
            line = line + 1

def updateSheet(busList, worksheet):
    lastLine = 1
    for element in busList:
    #print(element[0])
        for key, value in element[1].items():
            lastLine = lastLine + 1

    updateRange = "A2:D" + str(lastLine)
    print(updateRange)

    cell_list = wks.range(updateRange)

    i = 0
    for element in busList:
        #print(element[0])
        for key, value in element[1].items():
            cell_list[i].value = element[0]
            i = i + 1
            cell_list[i].value = key
            i = i + 1
            cell_list[i].value = value[0]
            i = i + 1
            cell_list[i].value = value[1]
            i = i + 1
            print(element[0] + "  ", end="")
            print(key + " - " + str(value))

    range = "C" + str(2) + ":D" + str(i)
    worksheet.format(range, {"horizontalAlignment": "CENTER"})  
    worksheet.update_cells(cell_list)

sa = gspread.service_account("token.json")
print(sa)

sh = sa.open("Sumo Test")

wks = sh.worksheet("1")
#print(wks)

#webbrowser.open(sh.url)

lista = [
            ['l4_d05:03', {'l4_d05:06': [35, '5:19:56']}], 
            ['l4_d05:06', {'l4_d05:03': [35, '5:19:56'], 'l15_d05:29': [25, '5:32:50']}], 
            ['l15_d05:29', {'l4_d05:06': [25, '5:32:50'], 'l11_d05:28': [48, '5:36:09']}], 
            ['l11_d05:28', {'l15_d05:29': [48, '5:36:09']}], 
            ['l3_d05:17', {'l8_d05:21': [16, '5:44:20']}], 
            ['l8_d05:21', {'l3_d05:17': [16, '5:44:20'], 'l3_d05:37': [3, '5:44:32']}], 
            ['l3_d05:37', {'l8_d05:21': [3, '5:44:32']}]
        ]

#print(lista)

#print(wks.get_all_records())


#for che scorre prima lista
#for che scorre dizionario 
#variabile che tine conto della linea

print(next_available_row(wks))
wks.delete_rows(2, next_available_row(wks))

lastLine = 1
for element in lista:
    #print(element[0])
    for key, value in element[1].items():
        lastLine = lastLine + 1

updateRange = "A2:D" + str(lastLine)
print(updateRange)

cell_list = wks.range(updateRange)

# i = 0
# for element in lista:
#     #print(element[0])
#     for key, value in element[1].items():
#         cell_list[i].value = element[0]
#         i = i + 1
#         cell_list[i].value = key
#         i = i + 1
#         cell_list[i].value = value[0]
#         i = i + 1
#         cell_list[i].value = value[1]
#         i = i + 1
#         print(element[0] + "  ", end="")
#         print(key + " - " + str(value))


# range = "C" + str(2) + ":D" + str(i)
# wks.format(range, {"horizontalAlignment": "CENTER"})  
# wks.update_cells(cell_list)

updateSheet(lista, wks)


# line = 2
# for element in lista:
#     #print(element[0])
#     for key, value in element[1].items():
#         range = "C" + str(line) + ":D" + str(line)
#         wks.format(range, {
#             "horizontalAlignment": "CENTER"
#         })
#         #Bus Principale Col 1
#         wks.update_cell(line, 1, element[0])
#         #Bus Incontrato Col 2
#         wks.update_cell(line, 2, key)
#         #Tempo Connesso Col 3
#         wks.update_cell(line, 3, value[0])
#         #Orario d'incontro Col 4
#         wks.update_cell(line, 4, value[1])
#         print(element[0] + "  ", end="")
#         print(key + " - " + str(value))
#         line = line + 1
        


#print(line)        



#wks.update_cells("A2:", lista)
# wks.add_protected_range("A1:D1")
# wks.delete_columns(1,4)
#wks.batch_clear(["A2:"])