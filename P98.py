def swapFiles():
    file1 = input("Enter the name of the first file: ")
    file2 = input("Enter the name of the second file: ")
    with open(file1, 'r') as file1Content:
        b = file1Content.read()
    with open(file2, 'r') as file2Content:
        a = file2Content.read()
    with open(file1, 'w') as file1Content:
        file1Content.write(a)
    with open(file2, 'w') as file2Content:
        file2Content.write(b)


swapFiles()
