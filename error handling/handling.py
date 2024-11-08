import datetime, time
from math import floor
import time
from pathlib import Path

from nlib import novasroutines as nr, novastestvalues as nt
path = str(Path(__file__))
log = nr.logInit(path)

nr.infiniteCheck("enter your credit card number: ", "int", log, "Enter a number")
nr.infiniteCheck("enter your credit card number: ", "int", log)


