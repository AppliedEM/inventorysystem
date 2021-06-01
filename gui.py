from dbwrapper import dbwrapper
import json

with open('config.json', 'r') as f:
    confdat = json.loads(f.read())
#confdat['collectionname'] = 'test_collection'

def numquery(prompt, optionsarr):
    for i,j in enumerate(optionsarr):
        print('[' + str(i+1) + ']' + ':\t' + j)
    userinp = input(prompt)
    try:
        choice = int(userinp)-1
    except Exception as e:
        return -1, str(userinp)
    return choice, optionsarr[choice]

dbw = dbwrapper(confdat)

def mainfunc():
    choices = ['Insert', 'Search', 'Remove', 'Print database']
    index, choice = numquery('Please input the action you want to take, or (e)xit: ', choices)
    location = None
    if choice == 'Insert':
        name = str(input('Search for object, or select (n)ew: '))
        if not name == 'n':
            s = dbw.searchitems(name)
            #print([str(i['name']) + 'location: ' + str(i['location']) + 'quantity: ' + str(i['quantity']) for i in s])
            num,n = numquery('Select the item to use, or (c)ancel: ', ['name: ' + str(i['name']) + '\tlocation: ' + str(i['location']) + '\tquantity: ' + str(i['quantity']) for i in s])
            if not n == 'c':
                name = s[num]['name']
                location = s[num]['location']
            else:
                return
        else:
            name = input('Please enter the name of the new object: ')
            num,l = numquery('Please select the location to use, or choose (n)ew: ', dbw.getlocations())
            if not l == 'n':
                location = l
            else:
                location = str(input('Please select the new location of the object: '))
        quant = input('Please enter the quantity (1): ')
        if quant == '':
            dbw.insertitem(name, location)
        else:
            dbw.insertitem(name, location, quantity=float(quant))
    elif choice == 'Search':
        name = str. lower(input('Please input the name of the object you are trying to find: '))
        s = dbw.searchitems(name)
        print('searching for item: ', name)
        if len(s) == 0:
            print('Item not found, please use the insert option')
        for i in s:
            print(i)
    elif choice == 'Remove':
        name = str.lower(input('Please input the name of the object you are trying to remove: '))
        location = location = str(input('please input the location of the object: '))
        s = dbw.searchitems(name)
        options = [i['name'] + ': ' + i['location'] for i in s]
        sel, choice = numquery('Please enter your choice: ',options)
        quant = input('Please enter the quantity (1): ')
        if quant == '':
            dbw.removeitem(s[sel]['name'], s[sel]['location'])
        else:
            dbw.removeitem(s[sel]['name'], s[sel]['location'], quantity=float(quant))
        print('Item has been removed')
    elif choice == 'Print database':
        dbw.printdb()
    elif choice == 'e':
        print('Exiting. Thank you for using the management system.')
        exit(0)

def testnumquery():
    a = ['heather1','heather2','heather3']
    i, j = numquery('which heather would you like? ', a)
    print(i)
    print(j)

#testnumquery()
while True: mainfunc()
#test()
