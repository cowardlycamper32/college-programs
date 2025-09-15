class task_functions:
    def sum_odd(self):
        n = int(input("n = "))
        total = 0
        for i in range(1, n):
            print(i)
            if i % 2 != 0:
                print("Odd, adding to total.")
                total = total + i
            else:
                print("Even, ignoring value.")
        print("Total value:", total)
    def sum_digits(self):

object = task_functions()
object.sum_odd()