import random

print("*** This programm generates a random name for women! ***")

fem_first_name=['Magdalena', 'Anna', 'Małgorzata', 'Maria', 'Krystyna', 'Barbara', 'Teresa', 'Elżbieta', 'Janina', 'Zofia', 'Jadwiga', 'Danuta', 'Halina', 'Irena', 'Ewa', 'Helena', 'Grażyna']
fem_second_name=['Kowalska', 'Nowak', 'Wiśniewska', 'Wójcik', 'Kowalczyk', 'Kamińska', 'Lewandowska', 'Dąbrowska', 'Zielińska', 'Szymańska', 'Modrzewska']

men_first_name=['Robert', 'Filip', 'Daniel', 'Andrzej', 'Stefan', 'Piotr', 'Paweł']
men_second_name=['Kowalski', 'Nowak', 'Wiśniewski', 'Kowalczyk', 'Kamiński', 'Wieczorek']


answer=input("Do you want to generate a name for men or women? Answer W or M: ").upper()

if answer == 'W':
    fem_random_first_name=random.choice(fem_first_name)
    fem_random_second_name=random.choice(fem_second_name)
    print("Random female name is: %s %s" % (fem_random_first_name, fem_random_second_name))
elif answer == 'M':
    men_random_first_name=random.choice(men_first_name)
    men_random_second_name=random.choice(men_second_name)
    print("Random men name is: %s %s" % (men_random_first_name, men_random_second_name))
else:
    pass


while True:
    answer=input("Do you want to generate another random name? (Y/N?) ").upper()
    answer2=input("Do you want to generate another name for men or women? Answer W or M: ").upper()
    if answer=='Y':
        if answer2 == 'W':
            fem_random_first_name=random.choice(fem_first_name)
            fem_random_second_name=random.choice(fem_second_name)
            print("Random female name is: %s %s" % (fem_random_first_name, fem_random_second_name))
        elif answer2 == 'M':
            men_random_first_name=random.choice(men_first_name)
            men_random_second_name=random.choice(men_second_name)
            print("Random men name is: %s %s" % (men_random_first_name, men_random_second_name))
        else:
            pass
    else:
        break
