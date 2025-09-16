from pathlib import Path
from nlib import novasroutines as nr, novastestvalues as nt

path = str(Path(__file__))
log = nr.logInit(path)

nr.infiniteCheck("enter your credit card number: ", "int", log, "Invalid Input")
nr.infiniteCheck("enter your credit card number: ", "int", log)
