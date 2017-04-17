import csv

dictio = open('dictionary.csv')
dictionary = dictio.readlines()
dictio.close()
i = 1
mydict = {}
for i in range(len(dictionary)):
    # split string into 2 element (string and double string)
    dictionary[i] = dictionary[i].split(';', 1)
    # split double string into tuple
    dictionary[i][1] = tuple(dictionary[i][1].split(';'))
    mydict[dictionary[i][0]] = dictionary[i][1]  # adding items to dictionary
    i += 1
repeatmain = 1
while repeatmain == 1:
    a = input("""Dictionary for a little programmer:
            1) search explanation by appellation *
            2) add new definition
            3) show all appellations alphabetically
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
                print(
                    "\ndictionary doesn't include that word, try with another word:\n ")
    elif a == '2':
        newapp = input('Type an appellation:')
        newdef = input('Create a definition for the new appellation:')
        newsource = input('Provide a source of that definition:')
        newtuple = (newdef, newsource)
        mydict[newapp] = newtuple  # adding new key&value to mydict
        lista = []
        lista1 = []
        for line in mydict.items():  # turning dictionary into list of nested tuples,
            el1 = line[0]
            el2 = line[1]
            lista.append(el1)
            lista.append(el2)
        for element in lista:  # unnesting tuples into list of strings
            if isinstance(element, tuple):
                elx1 = element[0]
                elx2 = element[1]
                lista1.append(elx1)
                lista1.append(elx2)
            else:
                lista1.append(element)
        string = ''
        iterator = 0
        for element in lista1:  # turning list of strings into string
            string += element.rstrip()
            string += ';'
            iterator += 1
            if iterator % 3 == 0:
                string += '\n'
        print(string)
        newdict = open('dictionary.csv', 'w')  # writing highscore to the file
        newdict.write(string)
        newdict.close()

    elif a == '3':
        print()
        sortedkeys = sorted(mydict)
        i = 0
        for i in range(len(sortedkeys)):
            print(sortedkeys[i])
            i += 1
        print()
    elif a == '0':
        print("Have a nice day!")
        quit()
    else:
        print("Wrong option chosen, try again!!!!")
