from dataclasses import dataclass

@ dataclass
class Cromosoma:
    id : str
    cromosoma : int

    def __repr__(self):
        return f"{self.id}, {self.cromosoma}"

    def __str__(self):
        return f"{self.id}, {self.cromosoma}"
    def __hash__(self):
        return ((self.id), (self.cromosoma))
