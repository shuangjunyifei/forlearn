import xdrlib,sys
import xlrd,datetime
def open_excel(file):
    data = xlrd.open_workbook(file)
    return data

#convert time to string time foramt
def convert(a,b):
    #data = open_excel()
    #a1 = datetime.datetime(*xlrd.xldate_as_tuple(a,data.datemode))
    a1 = datetime.datetime(*xlrd.xldate_as_tuple(a,b))
    a1 = str(a1.strftime('%m'))
    #return a1
    return a1
def data(file,b,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    rowhead = table.row_values(0)#将表头属性进行读取 赋值！！
    colhead = table.col_values(14)#列头数据包含（0）【0】，读取，赋值
    colheads=[]
    country={}
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        #print (country[[row[14]])
        if row[14] not in colheads:
            colheads.append(row[14])
    #print(colheads)
    for i in colheads:                           #建立国家列表
        country[i]=[]

    for rownum in range(1,nrows):                #再次从头遍历
        row = table.row_values(rownum)
        country[row[14]].append(row[b])

    newamounts={}
    for k,v in country.items():
        newamounts[k]=sum(v)
        if newamounts[k]<50000:


    f=open("国家贸易金额.txt","w")
    f.write(str(newamounts))


    print (newamounts)
data(r'C:\Users\acer\Desktop\tst.xls',19)
