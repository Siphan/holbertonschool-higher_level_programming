# import uuid

class Car():

    def __init__(self, *args, **kwargs):

        if len(args) > 0 and isinstance(args[0], dict):
            hash = args[0]
            name = hash.get('name')
            brand = hash.get('brand')
            nb_doors = hash.get('nb_doors')
        else:
            name = kwargs.get('name')
            brand = kwargs.get('brand')
            nb_doors = kwargs.get('nb_doors')

        if name == None or not isinstance(name, str):
            raise Exception("name is not a string")
        if brand == None or not isinstance(name, str):
            raise Exception("brand is not a string")
        if nb_doors is <= 0(nb_doors, int):
            raise Exception("nb_doors is not > 0")

    def to_hash(self):
        return {'name': self.__name,
                'brand': self.__brand,
                'nb_doors': self.__nb_doors}
