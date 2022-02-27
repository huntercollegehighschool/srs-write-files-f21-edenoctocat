import shelve

option = input("Enter A or B: ").lower()

while option not in 'ab':
  print("That's not valid.")
  option = input("Enter A or B: ")

if option == 'a':
  import ASavetodb

elif option == 'b':
  import BQuizzes
  takequiz = input('Would you like to take the quiz? ')
  if takequiz == 'yes':
    fq = open('quiz1.txt', 'r')
    print('\n', fq.readline())
    myanswers = []
    for i in range(50):
      lines = ''
      for j in range(7):
        lines += fq.readline()
      print(lines)
      myanswers.append(input("Letter: "))
    fq.close()
    fa = open('answers1.txt', 'r')
    fa.readline()
    fa.readline()
    score = 0
    realanswers = []
    for i in range(50):
      fa.readline()
      thisline = fa.readline()
      answer = thisline[0]
      realanswers.append(answer)
      if myanswers[i] == answer:
        score += 2
    print('\nYour score is:', score, '%')
    print(myanswers)
    print(realanswers)