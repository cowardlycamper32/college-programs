import login, register
import usermanager as um
from nlib import novasroutines as nr, novastestvalues as nt
from nlib.novasroutines import simpwrite as sw
if not(nr.fileexistscheck("./users/users.usrs")):
    nr.createpath("./users")
    file = nr.createfile("./users/", "users.usrs")
else: file = open("./users/users.usrs", "a+")



nr.simpwrite(file, "admin:admin")

temp = um.usermanager(file)
usernames = next(temp)
password = next(temp)

print(usernames)
print(password)

