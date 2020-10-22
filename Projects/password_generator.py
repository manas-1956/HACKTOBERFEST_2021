import random

def passwdGen():
    # declartions
    pasList = []
    sLet = list('qwertyuiopasdfghjklzxcvbnmAZQWSXEDCRFVTGBYHNUJMIKOLP')
    sNum = list('1234567890!@#$%^&*()-_+=\'",.<>')
    # picks random elements from above list
    ranLet = random.sample(sLet, random.randint(3, 8))
    ranNum = random.sample(sNum, random.randint(4, 7))
    # adds random elements to pasList
    pasList.append(ranLet)
    pasList.append(ranNum)
    # make the sublist to a single list
    finalLis = []
    for i in pasList:
        for j in i:
            finalLis.append(j)
    # shuffles the list for strong password
    random.shuffle(finalLis)
    # adds a random letter in the begining
    firRan = str(random.choice(sLet))
    finalLis.insert(0, firRan)
    # converts the list to a str
    str1 = ''
    password = str1.join(finalLis)
    return "Here's your strong password: " + password

print(passwdGen())
