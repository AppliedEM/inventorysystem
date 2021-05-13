from dbwrapper import dbwrapper
import json

with open('config.json', 'r') as f:
    confdat = json.loads(f.read())
confdat['collectionname'] = 'test_collection'

def numquery(prompt, optionsarr):
    for i,j in enumerate(optionsarr):
        print('[' + str(i) + ']' + ':\t' + j)
    choice = int(input(prompt))
    return choice, optionsarr[choice]

dbw = dbwrapper(confdat)

# objective = input('What are you doing with the object?: ')

def test():
    choices = ['insert', 'search', 'remove']
    index, choice = numquery('Please input the action you want to take: ', choices)
    if choice == 'insert':
        print('you chose insert!')
        exit(0)
    location = input('please input the location of the object: ')

    dbw.insertitem(name, location)
    dbw.printdb()

def testnumquery():
    a = ['heather1','heather2','heather3']
    i, j = numquery('which heather would you like? ', a)
    print(i)
    print(j)

# testnumquery()
test()
