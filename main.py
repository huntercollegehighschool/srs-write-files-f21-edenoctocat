import shelve

option = input("Enter A or B: ").lower()

while option not in 'ab':
  print("That's not valid.")
  option = input("Enter A or B: ")

if option == 'a':
  import ASavetodb

elif option == 'b':
  import BQuizzes