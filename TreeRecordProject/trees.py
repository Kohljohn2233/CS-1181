# File Name: trees.py
# Date: 11/28/2021
# Class: CS 1181
# Name: Kohl Johnson
# Professor: Jon Holmes
# Description: Holds all the functions for creating tree object


class Tree:
    def __init__(self, tree_type: str, tree_variety: str):
        """Constructor function, sets/assigns starting variables"""
        self.type_tree = tree_type
        self.variety = tree_variety
        self.height = 0

    def getDescription(self):
        """Gets description of the tree and returns it in formatted string"""
        description = "{:<10}{:<20}{:<10}{:<10}\n".format(self.type_tree, self.variety, str(self.height) + "ft", "N/A")
        return description


class Pine(Tree):
    def __init__(self, tree_variety: str, cluster=2):
        """Constructor function for Pine tree"""
        self.type_tree = "Pine"
        self.needles = cluster
        super().__init__(self.type_tree, tree_variety)

    def getDescription(self):
        """Gets description of the pine tree"""
        description = "{:<10}{:<20}{:<10}{:<10}\n".format(self.type_tree, self.variety, str(self.height) + "ft", str(self.needles))
        return description


class WhitePine(Pine):
    def __init__(self):
        """Constructor function for white pine tree"""
        self.variety = "White"
        self.needles = 5
        super().__init__(self.variety, self.needles)


class Fir(Tree):
    def __init__(self, variety: str):
        """Constructor function for Fir tree"""
        self.type_tree = "Fir"
        self.variety = variety
        super().__init__(self.type_tree, self.variety)


class Aspen(Tree):
    def __init__(self, variety: str):
        self.type_tree = "Aspen"
        self.variety = variety
        super().__init__(self.type_tree, self.variety)


def get_starting_records() -> list:
    """Gets the starting record"""
    record = [
        Pine("Ponderosa"),
        WhitePine(),
        Fir("Fraser"),
        Aspen("Quaking"),
        Tree("Maple", "Sugar")
    ]

    return record
