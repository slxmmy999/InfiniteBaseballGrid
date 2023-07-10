from BaseballData import BaseballData
from GameCategories import GameCategories

categories = GameCategories()
categories = categories.get_grid()

print(categories)