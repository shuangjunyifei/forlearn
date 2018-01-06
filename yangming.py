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
    a1 = str(a1.strftime('%Y/%m/%d'))
    #return a1
    return a1


def data(file,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    rowhead = table.row_values(0)#将表头属性进行读取 赋值！！
    colhead = table.col_values(0)#列头数据包含（0）【0】，读取，赋值
    colheads=[]
    for i in colhead[1:]:
        j=int(i)
        colheads.append(j)
    days=list(set(colheads))
    days =[convert(day,data.datemode) for day in days]
    print (len(days))
    amounts={}
    for i in range(len(days)):
        amounts[days[i]]=[]
    print(amounts)
    exceptnumb =[]
    try:
        for rownum in range(1,nrows):
            row = table.row_values(rownum)
            print(convert(row[0],data.datemode))
            amounts[convert(row[0],data.datemode)].append(float(row[15]))
            if type(row[15])==str:
                print (row[0],row[15])
    except:
        exceptnumb.append(rownum)
        print("++++++++++++++++++++++++++++")
        print(exceptnumb)
            #for j in days)):
            #    if convert(row[0],data.datemode)==days[j]:
            #        amounts[days[j]].append(row[15])


    newamounts={}
    try:
        for k,v in amounts.items():
            newamounts[k]=sum(v)
            #print (jisuan)
            #amount[k]=sum(jisuan)
    except:
        print("error day",k,v)
    return exceptnumb
data(r'C:\Users\acer\Desktop\tst.xls')
