import pandas as pd

class menu():
    def __init__(self):
        pass
    def __str__(self):
        return "Main Menu"
    class submenu():
        def __init__(self):
            pass
        def __str__(self):
            return "Submenus"
        class StartMenu():
            def __init__(self):
                pass
            def __str__(self):
                return """
                """
        class bigmenu():
            def __init__(self):
                pass
            def __str__(self):
                return "Big Menu"


print(menu().submenu().StartMenu())