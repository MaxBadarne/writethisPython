import writetofile

def askme():
    """
    this program when ran will ask the user if he want to read write or clear the file
    read : this function will print out all the information that allready exist on the text file in the console fothe user to read 
    write : the user will be asked to  write something to the file after entering the command 
    clear : will clea te text file and delete all the content

    the programm will run ona  loop if not stopped, after each comand is successfully executed , a question will pop up asking if the user wants to continue with the programm
    if the user writes yes in many variations the programm  will start over asking the user what task to do 
    """
    check = False
    
    frage = input("what would you like to do, Read Write or Clear")
    frage = frage.strip().lower()

    if(frage =="clear"):
        writetofile.clear()
        askstop()
    if(frage =="write"):
        text = input("What would you like to write")
        writetofile.write(text)
        askstop()
    if(frage =="read"):
        writetofile.read()
        askstop()

def askstop():
    x = input("would you like to continue ? [yes,no]")
    x = x.strip().lower()
    if x == 'yes':
        askme()