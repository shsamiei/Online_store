userInfo = {'user' : 'shsamiei' , 'pass' : 'abc'}
userInfo2 = {'user' : 'alooali' , 'pass' : 'ali'}

userinfo3 = {'user' : 'aloeoali' , 'pass' : 'ali'}

listOfuser = []

listOfuser.append(userInfo)
listOfuser.append(userInfo2)


for i in listOfuser :
    if i['user'] == userinfo3['user'] : 
        print("Yesssss ! ")




