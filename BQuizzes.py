import shelve
import random

shelfFile = shelve.open('uscapitals')  # open file containing dictionary of US Capitals
capitals = shelfFile['capitals']  # stored dictionary

quizNum = 1

# .txt file names (you can modify if you wish, but careful how you do it)
quizname = 'quiz' + str(quizNum) + '.txt'
answerfile = 'answers' + str(quizNum) + '.txt'

# 1. Open 2 files that you will write to, a quiz and an answer key file
fquiz = open(quizname, 'w')
fanswers = open(answerfile, 'w')

# 2. Write headings on both files
fquiz.write('Capitals Quiz\n\n')
fanswers.write('Answers\n\n')

# the following creates a list of states, and then puts them in a random order
states = list(capitals.keys())
random.shuffle(states)  # reorder states for each quiz

for questionNum in range(50):  # loop through each of the 50 states
  correct = capitals[states[questionNum]]  # find correct capital from capitals dictionary; states[questionNum] is current state

  # create a list of possible wrong answers for the state
  wrong = list(capitals.values())  # start with all capitals
  
  # 3. Wrong currently contains all 50 capitals. You will need to remove the correct capital from that list.
  wrong.remove(correct)
  # OR
  # del <list>[<index>]

  # 4. A multiple choice quiz generally as a couple of wrong choices along with the correct choice. Create a list of multiple choice options. Start by randomly selecting 3 or 4 (or more, if you wish) wrong choices
  choices = random.sample(wrong, 4)

  # 5. Add the correct answer to your list of multiple choice options.
  choices.append(correct)

  # 6. Make sure you shuffle the options for the multiple choice (otherwise, the correct answer will always be the last choice)
  random.shuffle(choices)

  # 7. Write the question to the quiz (It should at least include the state itself and possibly the questions number)
  # Reminder: states[questionNum] is the current state
  fquiz.write(str(questionNum + 1) + '. What is the capital of ' + states[questionNum] + '?\n')

  # 8. Write the answer choices to the quiz. Choices are usually labeled A, B, C, D. It can be done with a loop (which is much easier), but doesn't have to be.
  letters = ['a) ', 'b) ', 'c) ', 'd) ', 'e) ']
  for (letter, choice) in zip(letters, choices):
    fquiz.write(letter + choice + '\n')
  fquiz.write('\n')

  # 9. Write the correct answer to the answer key file. It's up to you how you want to format it, but it probably should include the question number, the correct answer letter, and the correct capital.
  corletter = letters[choices.index(correct)]
  fanswers.write(str(questionNum + 1) + '. \n' + corletter + correct + '\n')
  
# 10. After completely writing both the quiz and the answer key, make sure to close both files.
fquiz.close()
fanswers.close()

# Hopefully you were able to generate one 50 question quiz. Can you modify this to generate multiple 50 question quizzes (hint: it does involve a loop)