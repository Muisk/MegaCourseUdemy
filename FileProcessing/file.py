def appendTxt2():
    with open ("first.txt","a+") as repeatText:
        repeatText.seek(0)
        bearCp = repeatText.read()
        repeatText.write(bearCp)
        repeatText.write(bearCp)
    

