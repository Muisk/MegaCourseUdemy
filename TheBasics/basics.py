"""""""""Basic"""""""""
def uppercase(*args):
    return sorted([i.upper() for i in args])

print(uppercase("zzz","aaa","bbb","ccc"))


def converter(data):     
    return [dat if not isinstance(dat,str) else 0 for dat in data]

def float_sum(data):     
    return sum([float(dat) for dat in data])

def converteres(data):     
    new_data = [dat for dat in data if dat != 'no data']
    return new_data

def foo(charact,filepath):
    myfile = open(filepath)    
    fk = myfile.read()
    ass= [i for i in fk if i == str(charact)]
    print (ass.count(charact))
    return ass

def rs(charact,filepath):
    myfile = open(filepath)    
    fk = myfile.read()
    return print (fk.count(charact))


"""""""""Files"""""""""
def files (charact,filepath):
    myfile = open(filepath)    
    fk = myfile.read()
    return print (fk.count(charact))

with open('test.txt','w') as myfile:
    myfile.write("tomatos")

def createfiles():
    with open ("test.txt") as bearText:
        firstText = bearText.read(90)
    with open('first.txt','w+') as myfile:
        myfile.write(firstText)

def appendTxt():
    with open ("bear2.txt") as bearText2:
        bearCp = bearText2.read()
    with open('bear1.txt','a+') as myfile:
        myfile.seek(0) #cursor en 0
        myfile.write(bearCp)

def appendTxt2():
    with open ("first.txt","a+") as repeatText:
        repeatText.seek(0)
        bearCp = repeatText.read()
        repeatText.write(bearCp)
        repeatText.write(bearCp)

