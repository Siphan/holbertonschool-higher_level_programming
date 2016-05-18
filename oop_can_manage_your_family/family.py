def Person(id, first_name, date_of_birth, genre, eyes_color): #Class definition

    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):

        def get_id (self):
            return self._id
            if type(id) < 0 | type(id) is not int:
                raise Exception("id is not an integer")
            self._id = id

        def get_first_name (self):
            return self._first_name
            if type(first_name) is NONE | type(first_name) is not str:
                raise Exception("string is not a string")
            self._first_name = first_name

        def get_date_of_birth (self):
            return self._date_of_birth
            if type(date_of_birth) not in list[int]:
                raise Exception("date_of_birth is not a valid date")
            self._id = id

        def get_genre (self):
            return self._genre
            if type(genre) is not str & type(genre) not in GENRES:
                raise Exception("genre is not valid")
            self._id = id

        def get_eyes_color (self):
            return self._eyes_color
            if type(eyes_color) is not type(eyes_color) | type(eyes_color) not in EYES_COLORS:
                raise Exception("date_of_birth is not a valid date")
            self._id = id

        def get_last_name (self):
            return self.last_name
            if type(last_name) is NONE | type(last_name) is not str:
                raise Exception("string is not a string")
            self.last_name = last_name
