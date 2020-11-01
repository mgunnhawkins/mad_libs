choice = int(input("Would you like mad libs 1,2,or 3?"))
if choice == 1:
    verb = input("Type a past tense verb.")
    adjective = input("Type an adjective.")
    noun = input("Type a noun.")

    print("Once there was a little {} who lived in the forest.".format(noun))
    print("The little {} {} so {} that they crashed through the cieling.  They hurt their head and had to find a nurse.  The end.".format(noun, verb, adjective))

elif choice == 2:
    color = input("Type a color.")
    verb = input("Type a past tense verb.")
    adjective = input("Type an adjective.")
    noun = input("Choose boy or girl.")

    print("One day the {} {} went swimming. The {} {} participated in a swimming race.".format(color, noun, color, noun))
    print("The {} {} was so {} that they won the swimming race." .format(color, noun, adjective)) 
    print("The {} {} got a gold medal. The end.".format(color, noun))
    
else:  
    print("done")
