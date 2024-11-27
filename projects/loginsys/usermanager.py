from nlib import novasroutines as nr, novastestvalues as nt, novasclasses as nc

def usermanager(userfile):
    temp = userfile.read()
    usernames = []
    passwords = []
    listofstuff = temp.split('\n')
    listofstuff2 = []
    for j in range(len(listofstuff)):
        listofstuff2.append(listofstuff[j].split(':'))
    for i in range(len(listofstuff2)):
        if i % 2 == 0 or i == 0:
            usernames.append(listofstuff2[i])
        else: passwords.append(listofstuff2[i])

    yield usernames
    yield passwords
