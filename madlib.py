# Make a madlib that prompts the user for 5 words/phrases
# and then adds those to a silly story.

madlib = "In the early 1900s, crossword "

plural_noun = input("Please give a plural noun: ")

madlib = madlib + plural_noun + " only appeared in children's books. Today, "

noun = input("Please give a noun: ")

madlib = madlib + noun + " puzzles are in almost every "

noun = input("Please give another noun: ")

madlib = madlib + noun + " printed in the U.S. and throughout the whole "

adjective = input("Please give an adjective: ")

madlib = madlib + adjective + " world. More people do crossword puzzles than smoke "

plural_noun = input("Please give another plural_noun: ")

madlib += plural_noun + " or drink "

plural_noun = input("Please give ANOTHER plural_noun: ")

madlib += plural_noun + "."

print(madlib)
