import xlrd,os


def read_execel(filename,index):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    print(sheet.nrows)
    print(sheet.ncols)
    dic = {}
    for j in range(sheet.ncols):
        data = []
        for i in range(sheet.nrows):
            data.append(sheet.row(i)[j])
        dic[j] = data
    return dic

if __name__ == '__main__':
    data = read_execel(os.path.split(os.path.realpath(__file__))[0].split('c')[0]+'data\\testdata.xlsx',0)
    print(data)
    print(data.get(1))