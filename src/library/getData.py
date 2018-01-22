import xlrd
from src.library.getRootPath import getRootPath

def getDataFromxls(filepath):
    filepath = getRootPath() + file
    all_test_data = []
    filedata = xlrd.open_workbook(filepath)
    # print(filedata)
    sheet = filedata.sheets()[0]
    filereader = sheet.nrows
    # print(filereader)


    for row in range(1,filereader):
        # print(row)
        all_test_data.append(sheet.row_values(row))



    return all_test_data
file = "/src/data/test_data.xlsx"
# print(getDataFromxls(file))




