# Name: Lily Britto
# VUnetID: brittolb
# Email: lily.b.britto@vanderbilt.edu
# Class: CS 1104 - Vanderbilt University
# Section: 1
# Date: 4/21/22
# Honor statement: I attest that I understand the honor code for this class and have neither 
#                  given nor received any unauthorized aid on this assignment.

# Program description: This program creates a class template to represent a person 
#                      and their children.


class Person:
    def __init__(self, name = 'N/A', birth_date = 'N/A', death_date = ''):
        """
        Initializes the person object.
        
        Parameters:
          name:
            The name of the person.
            
          birth_date:
            The birth date of the person.
            
          death_date:
            The death date of the person.
        """
        self.__name = name
        self.__birth_date = birth_date
        self.__death_date = death_date
        self.__parent = None
        self.__children = []

    def add_child(self, person):
        """
        Adds a child to the person's child list.
        
        Parameters:
          person:
            The person object representing the child to be added.
        """    
        person.__parent = self
        self.__children.append(person)

    def delete_child(self, name):
        """
        Deletes a child from the person's child list.
        
        Parameters:
          name:
            The name of the child to be deleted.
        """    
        for child in self.__children:
            if child.__name == name:
                child_to_delete = child   
                self.__children.remove(child_to_delete)

    def get_age(self):
        """
        Retrieves the age of the person object.
        
        Returns:
          The age of the person object.
        """    
        split_birth_date = self.__birth_date.split('-')
        split_death_date = self.__death_date.split('-')
        if int(split_birth_date[1]) == int(split_death_date[1]):
            if int(split_birth_date[2]) <= int(split_death_date[2]):
                return int(split_death_date[0]) - int(split_birth_date[0])
            else:
                return (int(split_death_date[0]) - int(split_birth_date[0])) - 1

        elif split_birth_date[1] < split_death_date[1]:
            return int(split_death_date[0]) - int(split_birth_date[0])

        elif split_birth_date[1] > split_death_date[1]:
            return (int(split_death_date[0]) - int(split_birth_date[0])) - 1

    def get_birth_date(self):
        """
        Retrieves the birth date of the person object.
        
        Returns:
          The birth date of the person object.
        """ 
        return self.__birth_date

    def get_child(self, name):
        """
        Retrieves a child from the person's child list.
        
        Parameters:
          name:
            The name of the child to be retrieved.
        
        Returns:
          The person object representing the child.
        """ 
        for child in self.__children:
            if child.__name == name:
                child_to_get = child   
        return child_to_get

    def get_children(self):
        """
        Retrieves the person's child list.
        
        Returns:
          The child list of the person.
        """ 
        return self.__children

    def get_death_date(self):
        """
        Retrieves the death date of the person object.
        
        Returns:
          The death date of the person object.
        """ 
        return self.__death_date

    def get_name(self):
        """
        Retrieves the name of the person object.
        
        Returns:
          The name of the person object.
        """ 
        return self.__name

    def get_parent(self):
        """
        Retrieves the parent of the person object.
        
        Returns:
          The parent of the person object.
        """ 
        return self.__parent

    def set_birth_date(self, birth_date):
        """
        Sets the birth date of the person object.
        
        Parameters:
          birth_date:
            The birth date to set for the person object.
        """ 
        self.__birth_date = birth_date

    def set_death_date(self, death_date):
        """
        Sets the death date of the person object.
        
        Parameters:
          death_date:
            The death date to set for the person object.
        """ 
        self.__death_date = death_date

    def set_name(self, name):
        """
        Sets the name of the person object.
        
        Parameters:
          name:
            The name to set for the person object.
        """ 
        self.__name = name

    def set_parent(self, parent):
        """
        Sets the parent of the person object.
        
        Parameters:
          parent:
            The parent to set for the person object.
        """ 
        self.__parent = parent

    def __str__(self):
        """
        Specifies the print method for the person object.
        
        Returns:
          A formatted string with the person's information.
        """ 
        if self.__death_date == '':
            return self.__name + ' *' + self.__birth_date

        else:
            age = str(Person.get_age(self))
            return self.__name + ' *' + self.__birth_date + ' ✝' + self.__death_date + ' (' + age + ')'

    def __eq__(self, other):
        """
        Determines if two objects are equal based on the set rules.
        
        Parameters:
          other:
            The other object to be compared with.
            
        Returns:
          True if equal or False if not equal.
        """ 
        if type(self) == type(other):
            if self.__name == other.__name:
                split_birth_date_self = self.__birth_date.split('-')
                split_birth_date_other = other.__birth_date.split('-')
                if split_birth_date_self[0] == split_birth_date_other[0]:
                    if split_birth_date_self[1] == split_birth_date_other[1]:
                        if self.__death_date == '' and other.__death_date == '':
                            return True
                        elif self.__death_date.split('-')[0] == other.__death_date.split('-')[0]:
                            if self.__death_date.split('-')[1] == other.__death_date.split('-')[1]:
                                return True
        return False