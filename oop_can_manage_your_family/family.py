import json
import os.path #Used to check if a file exists

'''Parent Class'''
class Person():

    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    '''Person Methods'''
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

    '''Setter'''
    def just_married_with(self):
        return self.__id

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

    '''
    Creates and returns a JSON-like dictionary (Python hash)
    with key-value pairs representing the attributes of a Person (or subclass) instance
    '''
    def json(self):
        desc = {
        'id' : self.__id,
        'eyes_color' : self.__eyes_color,
        'genre' : self.__genre,
        'date_of_birth' : self.__date_of_birth,
        'first_name' : self.__first_name,
        'last_name' : self.last_name,
        }

        '''
        If person is not married, sets their status to zero. Otherwise
        sets it to the id of the person they are married to.
        '''
        if hasattr(self, 'is_married_to'):
            desc['is_married_to'] = self.is_married_to
        else:
            desc['is_married_to'] = 0
        return desc

    '''Set the attributes of a Person (or subclass) instance according to the values of a hash'''
    def load_from_json(self, json):
        if type(json) != dict:
            Exception("json is not valid")
        '''
        Loops through json object, if a Person attribute is found,
        updates it based on its corresponding value in json object.
        '''
        for p in json:
            if p == "id":
                self.__id = json[p]
            if p == "first_name":
                self.__first_name = json[p]
            if p == "date_of_birth":
                self.__date_of_birth = json[p]
            if p == "genre":
                self.__genre = json[p]
            if p == "eyes_color":
                self.__eyes_color = json[p]
            if p == "last_name":
                self.last_name = json[p]

    def is_married(self):
        '''
        Check to see if attribute is_married_to does not equal zero. If it
        is zero, then the person is not married. Otherwise, the value will be
        the id of the person they are married to.
        '''
        if self.is_married_to == 0:
            return False
        else:
            return True

    def just_married_with(self, p):
        '''
        Assign' attribute is_married_to with the id of the person p. and
        vice versa, so that they are connected by id numbers
        '''
        if self.is_married_to != 0 or p.is_married_to != 0:
            raise Exception("Already married")
        if self.can_be_married() == False or p.can_be_married() == False:
            raise Exception("Can't be married")

        self.is_married_to = p.__id
        p.is_married_to = self.__id
        if p.__genre == "Female":
            p.last_name = self.last_name
        if self.__genre == "Female":
            self.last_name = p.last_name
    '''End of Person Methods'''


'''Subclasses'''
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
    def can_be_married(self):
        return False
    def can_have_child(self):
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
    def can_be_married(self):
        return False
    def can_have_child(self):
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
    def can_be_married(self):
        return True
    def can_have_child(self):
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
    def can_be_married(self):
        return True
    def can_have_child(self):
        return False

'''Global Methods'''
def load_from_file(filename):
    '''
    Check for file existence, and if it's found, open a file passed as
    filename and return Person objects (this does not return JSON objects).
    In this way, the JSON objects in the file can be used with methods in the
    Person class and its subclass if applicable.
    '''
    if type(filename) != str or os.path.isfile(filename) != True:
        raise Exception("filename is not valid or doesn't exist")
    with open(filename) as json_file:
        data = json.load(json_file)
    json_file.close()

    '''
    Generate an array of Person (or a corresponding subclass) objects from
    JSON objects.
    '''
    arr = []
    class_dict = {"Senior": Senior, "Adult": Adult, "Teenager": Teenager, "Baby": Baby}
    for i in range(0, len(data)):
        d = data[i]

        '''
        Loop through array, if the object is a subclass (i.e., it has a key
        of 'kind'), then generate a class with the value of kind (the class
        comes from the class_dict).
        '''
        j = 0
        for i in d:
            '''
            If the object has a key of 'kind', then we know this object
            if a subclass of Person. Thus generate an instance with its
            corresponding subclass. Otherwise create a Person instance.
            '''
            if i == 'kind':
                p = class_dict[d['kind']](d['id'], str(d['first_name']), d['date_of_birth'], str(d['genre']), str(d['eyes_color']))
                break
            if j + 1 == len(d):
                p = Person(d['id'], str(d['first_name']), d['date_of_birth'], str(d['genre']), str(d['eyes_color']))
            j = j + 1
        j = 0
        for i in d:
            '''
            If the object has a key of 'last_name', then the last name is
            already set. Otherwise we need to set it to an empty string in
            case we want to later turn it into a JSON object.
            '''
            if i == 'last_name':
                p.last_name = d['last_name']
                break
            if j + 1 == len(d):
                p.last_name = "unknown"
            j = j + 1
        j = 0
        for i in d:
            '''
            If the object has a key of 'last_name', then the last name is
            already set. Otherwise we need to set it to an empty string in
            case we want to later turn it into a JSON object.
            '''
            if i == 'is_married_to':
                p.is_married_to = d['is_married_to']
                break
            if j + 1 == len(d):
                p.is_married_to = 0
            j = j + 1
        arr.append(p)
    return arr

def save_to_file(list, filename):
    '''
    Iterate through a list. If the type is not a dict (meaning it is
    probably an inherited class object), then store the particular subclass
    in var kind. Then append the name of the subclass to the dict. Finally,
    open the filename that was passed as an argument and write the json
    data to the file.
    '''
    for i in range(0, len(list)):
        if type(list[i]) != dict:
            kind = type(list[i])
            list[i] = list[i].json()
            list[i]['kind'] = kind.__name__
    target = open(filename, 'w')
    list_dump = json.dumps(list)
    target.write(list_dump)
    target.close()
'''End of global Methods'''
