dictio = open('dictionary.csv')
dictionary = dictio.readlines()
dictio.close()
i = 1
mydict = {}
for i in range(len(dictionary)):
    dictionary[i] = dictionary[i].split(';', 1) #split string into 2 element (string and double string)
    dictionary[i][1] = tuple(dictionary[i][1].split(';')) #split double string into tuple
    mydict[dictionary[i][0]] = dictionary[i][1] #adding items to dictionary
    i += 1
repeatmain = 1
while repeatmain == 1: 
    a = input("""Dictionary for a little programmer:
            1) search explanation by appellation *
            2) add new definition
            3) show all appellations alphabetically
            4) show available definitions by first letter of appellation **
            0) exit\n""")
    if a == '1':
        repeat1 = 1
        while repeat1 == 1:
            word = input("type a word to search: ")
            if word in mydict:
                repeat1 = 0
                mydict.get(word)
                expl = mydict.get(word)[0]
                source = mydict.get(word)[1]
                print(expl, 'source:', source)
            else:
                print("\ndictionary doesn't include that word, try with another word:\n ")
    elif a == '2':
        newapp = input('Type an appellation:')
        newdef = input('Create a definition for the new appellation:')
        newsource = input('Provide a source of that definition:')
        newtuple = (newdef, newsource) 
        mydict[newapp] = newtuple #adding new key&value to mydict
        lista = []
        for line in mydict.items(): #turning dictionary into list of nested tuples
            for element in line: #failed to turn list of nested tuples into csv file :(
                lista.append(line)
        print(lista)
    elif a == '3':
        sortedkeys = sorted(mydict)
        i = 1
        for i in range(len(sortedkeys)):
            print(sortedkeys[i])
            i += 1
    elif a == '0':
        print("Have a nice day!")
        quit()
    else:
        print("Wrong option chosen, try again!!!!")










