from dbwrapper import dbwrapper
import json

with open('config.json', 'r') as f:
    confdat = json.loads(f.read())
confdat['collectionname'] = 'test_collection'

def numquery(prompt, optionsarr):
    for i,j in enumerate(optionsarr):
        print('[' + str(i+1) + ']' + ':\t' + j)
    choice = int(input(prompt))-1
    print(choice, optionsarr[choice])
    return choice, optionsarr[choice]

dbw = dbwrapper(confdat)

def test():
    choices = ['Insert', 'Search', 'Remove', 'Print database']
    index, choice = numquery('Please input the action you want to take: ', choices)
    if choice == 'Insert':
        name = str(input('Please input the name of the oject: '))
        location = str(input('please input the location of the object: '))
        dbw.insertitem(name, location)
        dbw.printdb()
    elif choice == 'Search':
        name = str. lower(input('Please input the name of the oject you are trying to find: '))
        s = dbw.searchitems(name)
        print('searching for item: ', name)
        if len(s) == 0:
            print('Item not found, please use the insert option')
        for i in s:
            print(i)
    elif choice == 'Remove':
        name = str.lower(input('Please input the name of the oject you are trying to remove: '))
        location = location = str(input('please input the location of the object: '))
        s = dbw.searchitems(name)
        for i in s:
            dbw.removeitem(name, location)
            print('Item has been removed')
    elif choice == 'Print database':
        dbw.printdb()

def testnumquery():
    a = ['heather1','heather2','heather3']
    i, j = numquery('which heather would you like? ', a)
    print(i)
    print(j)

#testnumquery()
#while True: test()
test()
