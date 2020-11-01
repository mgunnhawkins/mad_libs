

mad_libs_1 = """Mad libs 1- Once there was a little {} who lived in the forest. The {} {} went so {} that they crashed through the cieling.  
They hurt their head and had to find a nurse.  The end.\n"""

mad_libs_2 = """Mad Libs 2- One day the {} {} went swimming. The {} {} participated in a swimming race.  
The {} {} was so {} that they won the swimming race. The {} {} got a gold medal. The end.\n"""

mad_libs_3 = """Mad Libs 3- The {} {} went over the river to {} their Grandma."""
print(mad_libs_1)
print(mad_libs_2)
print(mad_libs_3)

choice = input("Would you like:\n Mad Libs 1, \n Mad Libs 2, or \n Mad Libs 3? \n")
if choice == "Mad Libs 1":
    verb = input("Type a past tense verb.")
    adjective = input("Type an adjective.")
    noun = input("Type a noun.")
    print(mad_libs_1.format(noun, adjective, noun, verb))
elif choice == "Mad Libs 2":
    color = input("Type a color.")
    verb = input("Type a past tense verb.")
    adjective = input("Type an adjective.")
    noun = input("Choose boy or girl.")
    feeling = input("Name a feeling.")
    print(mad_libs_2.format(adjective, noun, adjective, noun, adjective, noun, feeling, adjective, noun))
else:  
    adjective = input("Type an adjective.")
    noun = input("Choose boy or girl.")
    verb = input("Type a past tense verb.")
    print(mad_libs_3 .format(adjective, noun, verb))

