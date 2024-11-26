import login, register
from nlib import novasroutines as nr, novastestvalues as nt

file = nr.createfile("./users/users.usrs")

nr.simpwrite(file, "admin:admin")

