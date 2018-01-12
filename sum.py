import xdrlib,sys
import xlrd
def open_excel(file=r'C:\Users\acer\Desktop\asd.xlsx'):
    data = xlrd.open_workbook(file)
    return data
def data(file,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    rowhead = table.row_values(0)#将表头属性进行读取 赋值！！
    colhead = table.col_values(0)
    print(colhead)#列头数据包含（0）【0】，读取，赋值
    colheads=[]
    for i in colhead[1:]:
        j=int(i)
        colheads.append(j)
    days=list(set(colheads))
    print (len(days))
    amounts={}
    amount={}
    jisuan=[]
    for i in range(len(days)):
        amounts[days[i]]=[]
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        for j in range(len(days)):
            if row[0]==days[j]:
                amounts[days[j]].append((row[15]))
    for k in amounts:
        jisuan=amounts[k]
        #print (jisuan)
        amount[k]=sum(jisuan)
    return amount
data(r'C:\Users\acer\Desktop\tst.xls')
