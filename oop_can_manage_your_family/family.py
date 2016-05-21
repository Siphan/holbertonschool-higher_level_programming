#from datetime import date

'''Parent Class'''
class Person():

    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    '''Constructor'''
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):

        '''Exceptions'''
        '''Define private attributes'''
        if id < 0 or type(id) is not int:
            raise Exception("id is not an integer")
        self.__id = id

        if type(first_name) is None or type(first_name) is not str:
            raise Exception("string is not a string")
        self.__first_name = first_name

        if(len(date_of_birth) is not 3 and all(isinstance(item, int) for item in date_of_birth)):
            raise Exception("date_of_birth is not a valid date")
        self.__date_of_birth = date_of_birth

        if isinstance(genre, str) and genre not in Person.GENRES:
            raise Exception("genre is not valid")
        self.__genre = genre

        if isinstance(eyes_color, str) and eyes_color not in Person.EYES_COLORS:
            raise Exception("eyes_color is not valid")
        self.__eyes_color = eyes_color

        '''Define public attribute'''
        self.last_name = "" # Syntax to let Python know that last_name is a string

    '''Getters'''
    def get_id (self):
        return self.__id
    def get_first_name (self):
        return self.__first_name
    def get_date_of_birth (self):
        return self.__date_of_birth
    def get_genre (self):
        return self.__genre
    def get_eyes_color (self):
        return self.__eyes_color

    '''Public methods'''
    '''Returns the full name of the person'''
    def __str__(self):
        return self.__first_name + " " + self.last_name

    '''Checks if person is male'''
    def is_male(self):
        if self.__genre is "Male":
            return True
        else:
            return False

    '''Returns age based on today's date and date of birth'''
    def age(self):
        return age
    def age(self):
        date = [5, 20, 2016]
        if self.__date_of_birth[0] >= date[0]:
            if self.__date_of_birth[1] > date[1]:
                return date[2] - (self.__date_of_birth[2] + 1)
            else:
                return date[2] - self.__date_of_birth[2]
        else:
            return date[2] - self.__date_of_birth[2]

'''Children Classes'''
class Baby(Person):
    pass
    def can_run(self):
        return False
    def need_help(self):
        return True
    def is_young(self):
        return True
    def can_vote(self):
        return False

class Teenager(Person):
    pass
    def can_run(self):
        return True
    def need_help(self):
        return False
    def is_young(self):
        return True
    def can_vote(self):
        return False
        
class Adult(Person):
    pass
    def can_run(self):
        return True
    def need_help(self):
        return False
    def is_young(self):
        return False
    def can_vote(self):
        return True

class Senior(Person):
    pass
    def can_run(self):
        return False
    def need_help(self):
        return True
    def is_young(self):
        return False
    def can_vote(self):
        return True
