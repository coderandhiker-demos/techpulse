
class Pokemon():
    def __init__(self, base_experience, height, id, name, weight, **kwargs):
        self.base_experience = base_experience
        self.height = height
        self.id = id
        self.name = name
        self.weight = weight
        self.__dict__.update(kwargs)