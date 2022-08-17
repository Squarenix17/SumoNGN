import gspread
import webbrowser



def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

def updateSheet(busList):
    lastLine = 1
    for element in busList:
    #print(element[0])
        for key, value in element[1].items():
            lastLine = lastLine + 1

    updateRange = "A2:D" + str(lastLine)
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
            #print(element[0] + "  ", end="")
            #print(key + " - " + str(value))

    range = "C" + str(2) + ":D" + str(i)
    wks.format(range, {"horizontalAlignment": "CENTER"})  
    wks.update_cells(cell_list)




sa = gspread.service_account("token.json")
print("Apertura Foglio di Calcolo in Corso!")
#print(sa)

sh = sa.open("Sumo Data")

wks = sh.sheet1
webbrowser.open(sh.url)

header = ["Bus Principale", "Bus Incontrato", "Tempo Connesso", "Orario d'incontro"]
range = "A1:D1"
wks.update(range, [header])
wks.columns_auto_resize(0,4)

wks.format(range,  {"backgroundColor": {  #color mapped 0.0 to 1
                                "red": 0.788,
                                "green": 0.8588,
                                "blue": 0.976
                                },
                    "horizontalAlignment": "CENTER",            
                    "textFormat": {
                                "bold": True
                                }
})


range =  "A2:D" + str(next_available_row(wks))
wks.batch_clear([range])
#wks.delete_rows(2, next_available_row(wks))
