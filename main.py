import math
from datetime import date

today = date.today()
print("Today's date:", today)
def dividers():
    print("\033[96m{}\033[0m".format("--------------------------------"))
    numb = int(input("What Number do you want: "))
    print("\033[96m{}\033[0m".format("--------------------------------"))
    print("Divisors:")
    summen = []
    for i in range(1, numb + 1):
        if (numb % i == 0):
            summen.append (i)
            print(i)

    print("\033[96m{}\033[0m".format("--------------------------------"))
    a = sum(summen)
    print ("All summa :",end = " ")
    print (a)
    f = open("summa.txt", "w")
    f.write("date: " + format(today))
    f.write("\n")
    f.write("Divisors:")
    f.write(format(i))
    f.write("\n")
    f.write("summa:" + format(a))

def reversrs():
  print("\033[96m{}\033[0m".format("--------------------------------"))
  Number1 = int(input("What is your first number: "))
  Number2 = int(input("What is your second number: "))
  print("\033[96m{}\033[0m".format("--------------------------------"))
  summa = range(Number1, Number2 + 1)
  Divisors = []
  Free = []
  answer = []
  for g in summa:
    Divisors.append(g)

  print("Dis is yours range: ", Divisors)
  print("\033[91m{}\033[0m".format("--------------------------------"))

  for pain in Divisors:
    for i in range(1, Divisors[len(Divisors) - 1] + 1):
      g = 0
      if pain % i == 0:
        Free.append(i)
      answer = []

  for i in Free:
    if i not in answer:
      answer.append(i)

    print("all integer divisors: ", sorted(answer))
    f = open("summa.txt", "w")
    f.write("date: " + format(today))
    f.write("\n")
    f.write("Dis is yours range: " + format(Divisors))
    f.write("\n")
    f.write("all integer divisors: " + str(sorted(answer)))



def main():

    if __name__ == '__main__':
        choice = input("\033[93m Good afternoon, you are on my code, here you can know all the divisors of a given number, healthy numbers and their sum.\n"
                    "\033[97m Ievadi burtu:\n"
                    "\033[94mFunction 1 - which you will know all the divisors and the sum of them \033[91mif you need this function write (d) \n"
                    "\033[94mFunction 2 - the logic stays the same, only the number of numbers changes from one number to another.\033[91mif you need this function write (r)")
        if choice.lower() == 'd':
            dividers()
        if choice.lower() == 'r':
            reversrs()
        

while True:
       main()
       restart = input('\033[97mdo you want again?').lower()
       if restart == "yes":
           main()
       else:
           print("\033[91mGoodbye")
           exit(0)

