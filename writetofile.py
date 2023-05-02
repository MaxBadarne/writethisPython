def write(text):
    x = open("text.txt", "a")
    x.write(text)
    x.close()
    print("successfully written to file ")

def read():
    x = open("text.txt", "r")
    temp = x.read()
    print("content of the files are : \n")
    print(temp)
    x.close()
    

def clear():
    x = open("text.txt", "w")
    x.write(" ")
    print("file sucessfully cleared")
    x.close
