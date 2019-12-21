def foo(charact,filepath):
    myfile = open(filepath)    
    fk = myfile.read()
    return print (fk.count(charact))

with open('test.txt','w') as myfile:
    myfile.write("tomatoss")