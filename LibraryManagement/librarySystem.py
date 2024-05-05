import json

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False
