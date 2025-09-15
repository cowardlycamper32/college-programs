from sys import argv

class Info:
    def __init__(self):
        self.version = "1.0.0"

    def ver(self):
        return self.version

    def help(self, args):
        if "-S" in args:
            print("""install command
            """)
        else:
            print("""usage:  tet.py <operation> [...]
operations:
    tets.py {-h --help}
    tets.py {-v --version}
    tets.py {-S} <options> <package(s)>
    more TBD""")


info = Info()
if "--help" in argv or "-h" in argv:
    info.help(argv)
if "--version" in argv or "-v" in argv:
    print(info.ver())