def swapFileData():
    file1 = input("Write the first file: ")
    file2 = input("Write the second file: ")
    with open(file1,'r') as a:
        data_a = a.read()

    with open(file2,'r') as b:
        data_b = b.read()

    with open(file1,'w') as a:
        a.write(data_b)

    with open(file2,'w') as b:
        b.write(data_a)

swapFileData()

