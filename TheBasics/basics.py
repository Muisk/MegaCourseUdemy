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
