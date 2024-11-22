from nlib import novasroutines as nr, novastestvalues as nt

if not(nr.fileexistscheck("./pswds/pass.pss")):
    nr.createpath("pswds")
    file = nr.createfile("./pswds/pass.pss")
else:
    file = open("./pswds/pass.pss")

