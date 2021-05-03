'''
title: dbwrapper.py
author: virtualalchemy
date: 5/1/2021
summary: wraps the database used by the program and allows for easy manipulation
    of data from the database
'''

import json
import pymongo
import datetime as dt
import re

divider = '---------------------------------'

class dbwrapper:
    def __init__(self, configjson):
        self.configdat = configjson
        self.dbclient = pymongo.MongoClient(self.configdat['dburl'])
        self.db = self.dbclient[self.configdat['dbname']]
        self.colname = self.configdat['collectionname']

    def printdb(self):
        col = self.db[self.colname]
        for i in col.find():
            print(i)

    def searchitems(self, itemname):
        '''
        search the items in the db for entries matching <itemname>
        inputs:
            itemname (string): name of the item to search for
        returns:
            (dict[]): array of dictionary objects containing the search restults
        '''
        col = self.db[self.colname]
        itemname = itemname.lower()
        print('searching:',itemname)
        items = []
        for i in col.find():
            if re.search(itemname, i['name'], re.IGNORECASE):
                items.append(i)
        return items

    def delete_all(self):
        '''
        WARNING: deletes all items in the working collection in the db
        '''
        col = self.db[self.colname]
        return col.delete_many({})

    def insertitem(self, itemname, storagelocation, quantity=1):
        '''
        inserts an item into the db. if an item with the same name in the same
        location exists, increment the quantity by the specified quantity.
        updates the modified_date entry every time it updates an entry
        inputs:
            itemname (string): name of the item to insert
            storagelocation (string): name of the inventory to insert into
        returns:
            (bool): whether the insert was successful or not
        '''
        col = self.db[self.colname]
        itemname = itemname.lower()
        storagelocation = storagelocation.lower()
        filter = {'name': itemname, 'location': storagelocation}
        existingitems = col.find(filter)
        if existingitems.count() > 0:
            newitem = existingitems[0]
            newitem['quantity'] += quantity
            newitem['modified_date'] = str(dt.datetime.now())
            col.replace_one(filter, newitem)
        else:
            dict = {"name": itemname, "location": storagelocation, 'quantity': 1, "created_date": str(dt.datetime.now()), "modified_date": str(dt.datetime.now())}
            x = col.insert_one(dict)
            return True
        return False

    def removeitem(self, itemname, storagelocation, quantity=1):
        '''
        removes an item from the db. if an item with the same name in the same
        location exists, decrement the quantity by the specified quantity
        inputs:
            itemname (string): name of the item to insert
            storagelocation (string): name of the inventory to insert into
        returns:
            (bool): whether the removal was successful or not
        '''
        col = self.db[self.colname]
        itemname = itemname.lower()
        storagelocation = storagelocation.lower()
        filter = {'name': itemname, 'location': storagelocation}
        existingitems = col.find(filter)
        if existingitems.count() > 0:
            newitem = existingitems[0]
            newitem['quantity'] -= quantity
            newitem['modified_date'] = str(dt.datetime.now())
            if newitem['quantity'] <= 0:
                col.delete_one(filter)
                return True
            else:
                col.replace_one(filter, newitem)
                return True
        return False

with open('config.json', 'r') as f:
    confdat = json.loads(f.read())
confdat['collectionname'] = 'test_collection'

def inserttest(delete=True):
    dbw = dbwrapper(confdat)
    print(divider)
    print('before inserting in loc1:')
    dbw.printdb()
    print(divider)
    print('after inserting in loc1:')
    dbw.insertitem('testitem1', 'box1')
    dbw.printdb()
    print(divider)
    print('after inserting new item in loc1')
    dbw.insertitem('testitem2', 'box1')
    dbw.printdb()
    print(divider)
    print('after inserting additional item in loc1:')
    dbw.insertitem('testitem1', 'box1')
    dbw.printdb()
    print(divider)
    print('after inserting in loc2:')
    dbw.insertitem('testitem1', 'box2')
    dbw.printdb()
    print(divider)
    print('after inserting new item in loc2:')
    dbw.insertitem('testitem2', 'box2')
    dbw.printdb()
    if delete:
        print('cleaning up...')
        dbw.delete_all()

def searchtest():
    inserttest(False)
    dbw = dbwrapper(confdat)
    s = dbw.searchitems('testitem')
    print(divider)
    print('searching for testitem:')
    for i in s:
        print(i)
    dbw.delete_all()

def removetest():
    inserttest(False)
    print(divider)
    print('attempting delete in loc1:')
    dbw = dbwrapper(confdat)
    dbw.removeitem('testitem1', 'box1')
    dbw.printdb()
    print(divider)
    print('attempting again...')
    dbw.removeitem('testitem1', 'box1')
    dbw.printdb()
    dbw.delete_all()

def deletealltest():
    dbw = dbwrapper(confdat)
    print('db contents before delete')
    dbw.printdb()
    print(divider)
    print('db contents after delete')
    x = dbw.delete_all()
    dbw.printdb()
    print('items deleted:',x)

#searchtest()
#inserttest()
#removetest()
#searchtest()
#deletealltest()
