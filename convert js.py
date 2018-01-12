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
    a1 = a1.strftime('%m')
    #return a1
    return a1            #转换数据，返回 月份。

def data(file,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    rowhead = table.row_values(0)#将表头属性进行读取 赋值！！
    colhead = table.col_values(0)#列头数据包含（0）【0】，读取，赋值
    colheads=[]
    for i in colhead[1:]:
        colheads.append(i)
    days=list(set(colheads))
    days =[convert(day,data.datemode) for day in days]
    months=sorted(list(set(days)))
    #print (months)                               #整合月份并进行字符串排序



    #dic={}
    #abbb=['countrysss','monthsss','series']
    #for i in abbb:
    #    dic[i]=[]                                #建立大字典
    #for i in months:
#        dic['monthsss'].append(i)


    country={}
    for rownum in range(1,nrows):
        row=table.row_values(rownum)
        country[row[14]]={}              #建立国家字典
    #print(country)
        for i in months:
            country[row[14]][i]=[]
    #print (country)                     #建立国家字典中月份列表
    #exceptnumb =[]
    #try:
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        #print (country[[row[14]])
        country[row[14]][convert(row[0],data.datemode)].append(row[15])
    #print (country)
                                         #国家字典中月份列表元素填充
    #newamounts={}
    #print (len(country))#try:
    #for i in range((12*len(country))):
#        dic['series'].append(i)
#    for i in range((12*len(country))):
#        dic['series'][i]=[]                 #建立series中空列表


#    for i in range(len(country)):
#        dic['countrysss'].append(country[i])

#        dic['series'][].append(country[i])
    for k,v in country.items():

#            dic['series'][0].append(k)
        country[k]=sum(v)                 #sum()计算；
            #print (jisuan)
            #amount[k]=sum(jisuan)


    #except:
    #    print("error day",k,v)

    f=open("国家.txt","w")
    f.write(str(country))
    return
data(r'C:\Users\acer\Desktop\tst.xls')
