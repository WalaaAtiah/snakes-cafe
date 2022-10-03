
welcam = """
****************************************
**    Welcome to the Snakes Cafe!     **
**    Please see our menu below.      **
**                                    **
** To quit at any time, type "quit"   **
****************************************
Appetizers 
----------
Wings
Cookies
Spring Rools

Entrees
-------
Salmon
Steak
Meat Tornado
Aliteral Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""
y = ""


def acknowledgment(x, q):
    a = 0
    Menu[x] += 1

    for i in Menu:
        if a==0:
             if Menu[i] == 1:
                q += "%s order of %s " % (Menu[i], i)
                a+=1
               # print("%s order of %s have been added to you meal"%(Menu[i],i))       
             elif Menu[i] > 1:
                 q += "%s orders of %s " % (Menu[i], i)
                 a+=1
            #    print("%s orders of %s have been added to you meal"%(Menu[i],i))
        else :
            if Menu[i] == 1:
                q += "and %s order of %s " % (Menu[i], i)
               
            elif Menu[i] > 1:
                 q += "and %s orders of %s " % (Menu[i], i)
           

           

    q += "have been added to you meal"
    print(q)


Menu = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rools": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "Aliteral Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0
}

print(welcam)
while True:
    order = input(">")
    if order in Menu:
        # print("true")
        acknowledgment(order, y)

    else:
        if order == "quit":
            break
        else:
            print("Please enter from the Menu")
