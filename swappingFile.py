def swapFileData():
    #variable a's text is being stored in the variable, "data_a"
    a=open("test.txt",'r')
    data_a = a.read()

    #variable b's text is being stored in the variable, "data_b"
    b=open("sample2.txt",'r')
    data_b = b.read()

    #variables data_a and data_b are being written in new variables that hold each other's files
    a2 = open("test.txt","w")
    a2.write(data_b)
    b2 = open("sample2.txt","w")
    b2.write(data_a)

swapFileData()