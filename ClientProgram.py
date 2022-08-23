# Name: Lily Britto
# VUnetID: brittolb
# Email: lily.b.britto@vanderbilt.edu
# Class: CS 1104 - Vanderbilt University
# Section: 1
# Date: 4/22/22
# Honor statement: I attest that I understand the honor code for this class and have neither 
#                  given nor received any unauthorized aid on this assignment.

# Program description: This program instantiates Person objects through various methods that
#                      as a whole represents a family.


from person import Person


def show_menu(current_person):
    """
    Shows the header and option menu and asks the user to select an option.
        
    Parameters:
      current_person:
        The person object of the person currently being looked at.
        
    Returns:
      The user-selected option number.
    """ 
    print('------------------------------------------------------')
    print(current_person)
    print('------------------------------------------------------')
    print(' 1) Edit name                 6) Print statistics')
    print(' 2) Edit date of birth        7) Print children')
    print(' 3) Edit date of death        8) Print grandchildren')
    print(' 4) Add a child               9) Print aunts/uncles')
    print(' 5) Delete a child           10) Print cousins\n')
    print('11) Enter child\'s family     12) Enter parent\'s family\n')
    option = int(input('Select option (or 0 to exit): '))
    print('')
    return option


def check_name():
    """
    Asks the user for a name until text is entered.

    Returns:
      The user-given name.
    """ 
    name = input('Enter name: ')
    while name == '':
        name = input('ERROR: No name entered, try again: ')
    return name


def check_date(date):
    """
    Checks the format of a given date and prints an error message until a valid date
    is entered.
    
    Parameters:
      date:
        The date to be checked.

    Returns:
      The date in the correct format.
    """ 
    date = date.split('-')
    while len(date) != 3 or len(date[0]) != 4 or len(date[1]) != 2 or len(date[2]) != 2:
        date = input('ERROR: Must follow 1970-01-01 format, try again: ')
        date = date.split('-')
    return '-'.join(date)


def option_one(current_person):
    """
    Carries out Option #1 by changing the name of the person object to the one
    given by the user.
        
    Parameters:
      current_person:
        The person object of the person currently being looked at.
    """ 
    name = check_name()
    current_person.set_name(name)


def option_two(current_person):
    """
    Carries out Option #2 by changing the date of birth of the person object to the one
    given by the user.
        
    Parameters:
      current_person:
        The person object of the person currently being looked at.
    """
    birth_date = input('Enter date of birth: ')
    birth_date = check_date(birth_date)
    current_person.set_birth_date(birth_date)


def option_three(current_person):
    """
    Carries out Option #3 by changing the date of death of the person object to the one
    given by the user.
        
    Parameters:
      current_person:
        The person object of the person currently being looked at.
    """
    death_date = input('Enter date of death: ')
    death_date = check_date(death_date)
    current_person.set_death_date(death_date)


def option_four(current_person):
    """
    Carries out Option #4 by adding a child with user-inputtted name and date of birth
    to the child list of the person object.
        
    Parameters:
      current_person:
        The person object of the person currently being looked at.
    """
    child_name = check_name()
    child_birth_date = input('Enter date of birth: ')
    child_birth_date = check_date(child_birth_date)
    child = Person(child_name, child_birth_date)
    children = current_person.get_children()
    for person in children:
        if Person.__eq__(child, person):
            print('ERROR: Child with same name, and year and month of birth already exists.')
            return

    current_person.add_child(child)


def option_five(current_person):
    """
    Carries out Option #5 by deleting a child with the user-given name from the child list
    of the person object.
        
    Parameters:
      current_person:
        The person object of the person currently being looked at.
    """
    children = current_person.get_children()
    if len(children) == 0:
        print('No children found for {}.'.format(current_person.get_name()))
        return

    for num in range(len(children)):
        print('{}) {}'.format(num+1, children[num].get_name()))

    option = int(input('Select a child (or 0 to go back to main menu): '))
    if option == 0:
        print('\nReturning to main menu.')
        return

    else:
        removed_child = children[option-1]
        current_person.delete_child(removed_child.get_name())
        print('\n{} deleted.'.format(removed_child.get_name()))


def option_six(current_person):
    """
    Carries out Option #6 by printing the number of children and grandchildren that
    the person object has.
        
    Parameters:
      current_person:
        The person object of the person currently being looked at.
    """
    children = current_person.get_children()
    grandchildren = []
    for person in children:
        grandchildren.extend(person.get_children())

    print('Number of children: {}'.format(len(children)))
    print('Number of grandchildren: {}'.format(len(grandchildren)))


def option_seven(current_person):
    """
    Carries out Option #7 by printing the names of the children of the person object, if any.
        
    Parameters:
      current_person:
        The person object of the person currently being looked at.
    """
    children = current_person.get_children()
    if len(children) == 0:
        print('No children found for {}.'.format(current_person.get_name()))
        return

    print('Children of {}:'.format(current_person.get_name()))
    for person in children:
        print('- {}'.format(person))


def option_eight(current_person):
    """
    Carries out Option #8 by printing the names of the grandchildren of the 
    person object, if any.
        
    Parameters:
      current_person:
        The person object of the person currently being looked at.
    """
    children = current_person.get_children()
    grandchildren = []
    for person in children:
        grandchildren.extend(person.get_children())

    if len(grandchildren) == 0:
        print('No grandchildren found for {}.'.format(current_person.get_name()))
        return

    print('Grandchildren of {}:'.format(current_person.get_name()))
    for person in grandchildren:
        print('- {}'.format(person))


def option_nine(current_person):
    """
    Carries out Option #9 by printing the names of the aunts and uncles of the 
    person object, if any.
        
    Parameters:
      current_person:
        The person object of the person currently being looked at.
    """
    parent = current_person.get_parent()
    if parent is None:
        print('No aunts and uncles found for {}.'.format(current_person.get_name()))
        return

    grandparent = parent.get_parent()
    if grandparent is None:
        print('No aunts and uncles found for {}.'.format(current_person.get_name()))
        return

    aunts_uncles = grandparent.get_children()
    aunts_uncles.remove(parent)

    if len(aunts_uncles) == 0:
        print('No aunts and uncles found for {}.'.format(current_person.get_name()))
        return

    print('Aunts and uncles of {}:'.format(current_person.get_name()))
    for person in aunts_uncles:
        print('- {}'.format(person))


def option_ten(current_person):
    """
    Carries out Option #10 by printing the names of the cousins of the 
    person object, if any.
        
    Parameters:
      current_person:
        The person object of the person currently being looked at.
    """
    parent = current_person.get_parent()
    if parent is None:
        print('No cousins found for {}.'.format(current_person.get_name()))
        return

    grandparent = parent.get_parent()
    if grandparent is None:
        print('No cousins found for {}.'.format(current_person.get_name()))
        return

    aunts_uncles = grandparent.get_children()
    for person in aunts_uncles:
        if person == parent:
            aunts_uncles.remove(parent)
    
    cousins = []
    for person in aunts_uncles:
        cousins.extend(person.get_children())

    if len(cousins) == 0:
        print('No cousins found for {}.'.format(current_person.get_name()))
        return

    print('Cousins of {}:'.format(current_person.get_name()))
    for person in cousins:
        print('- {}'.format(person))


def option_eleven(current_person):
    """
    Carries out Option #11 by entering the family of one of the children of 
    the person object.
        
    Parameters:
      current_person:
        The person object of the person currently being looked at.
        
    Returns:
      The updated current person being looked at (now a child of the previous).
    """
    children = current_person.get_children()
    if len(children) == 0:
        print('No children found for {}.'.format(current_person.get_name()))
        return current_person

    for num in range(len(children)):
        print('{}) {}'.format(num+1, children[num].get_name()))

    option = int(input('Select a child (or 0 to go back to main menu): '))
    if option == 0:
        print('\nReturning to main menu.')
        return current_person

    else:
        chosen_child = children[option - 1]
        current_person = chosen_child
        print('\nEntering family of {}.'.format(chosen_child.get_name()))
        return current_person


def option_twelve(current_person):
    """
    Carries out Option #12 by entering the family of the parent of the person object.
        
    Parameters:
      current_person:
        The person object of the person currently being looked at.
        
    Returns:
      The updated current person being looked at (now the parent of the previous).
    """
    parent = current_person.get_parent()
    if parent is None:
        print('No parent found for {}.'.format(current_person.get_name()))
        return current_person

    else:
        current_person = parent
        print('Entering family of {}.'.format(parent.get_name()))
        return current_person


def main():

    current_person = Person('John Doe', '1960-01-15', '2020-01-15')
    option = show_menu(current_person)

    while option != 0:
        if option == 1:
            option_one(current_person)
        elif option == 2:
            option_two(current_person)
        elif option == 3:
            option_three(current_person)
        elif option == 4:
            option_four(current_person)
        elif option == 5:
            option_five(current_person)
        elif option == 6:
            option_six(current_person)
        elif option == 7:
            option_seven(current_person)
        elif option == 8:
            option_eight(current_person)
        elif option == 9:
            option_nine(current_person)
        elif option == 10:
            option_ten(current_person)
        elif option == 11:
            current_person = option_eleven(current_person)
        elif option == 12:
            current_person = option_twelve(current_person)

        print('')
        option = show_menu(current_person)
        
    print('')
    
if __name__ == '__main__':
    main()