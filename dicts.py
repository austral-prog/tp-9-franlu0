def create_inventory(items):
    mydict=dict()
    for i in range(0,len(items)):
        if items[i] in mydict:
            mydict[items[i]]+=1
        else:
            mydict[items[i]]=1
    return mydict

def add_items(inventory, items):
    for key,value in enumerate(items):
        if value in inventory:
            inventory[value]+=1
        else:
            inventory[value]=1
    return inventory

def decrement_items(inventory, items):
    mydict = inventory
    for i,value in enumerate(items):
        if value in mydict and mydict[value]!=0:
            mydict[value]-=1
    return mydict

def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory

def list_inventory(inventory):
    listtodelete=[]
    mylist=[]
    for key, value in inventory.items():
        if value == 0:
            listtodelete.append(key)
    for i in listtodelete:
        del inventory[i]
    for key,value in inventory.items():
        mylist.append((key,value))  
    return mylist
