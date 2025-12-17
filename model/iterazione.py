from dataclasses import dataclass

@dataclass
class Iterazione():
    gene1 : str
    gene2 : str
    correlazione : int

    def __repr__(self):
        return f"{self.gene1}, {self.gene2}, {self.correlazione}"

    def __str__(self):
        return f"{self.gene1}, {self.gene2}, {self.correlazione}"

    def __hash__(self):
        return ((self.gene1), (self.gene2), (self.correlazione))