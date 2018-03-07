import random

print("*** This programm generates a random name for women! ***")

fem_first_name=['Magdalena', 'Anna', 'Małgorzata', 'Maria', 'Krystyna', 'Barbara', 'Teresa', 'Elżbieta', 'Janina', 'Zofia', 'Jadwiga', 'Danuta', 'Halina', 'Irena', 'Ewa', 'Helena', 'Grażyna']
fem_second_name=['Kowalska', 'Nowak', 'Wiśniewska', 'Wójcik', 'Kowalczyk', 'Kamińska', 'Lewandowska', 'Dąbrowska', 'Zielińska', 'Szymańska', 'Modrzewska']


random_first_name=random.choice(fem_first_name)
random_second_name=random.choice(fem_second_name)


print("Random name is: %s %s" % (random_first_name, random_second_name))

while True:
    answer=input("Do you want to generate another random name? (Y/N?) ")
    if answer=='Y':
        random_first_name=random.choice(fem_first_name)
        random_second_name=random.choice(fem_second_name)
        print("Your next random name is: %s %s" % (random_first_name, random_second_name))
    
    else:
        break

    






