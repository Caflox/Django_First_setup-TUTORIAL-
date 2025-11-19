from typing import Any
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(64)

    def __str__(self):
        return f"NAME: {self.name}, SURNAME: {self.surname}"
    
# class Teacher(models.Model):
#     name = models.CharField(256)
#     surname = models.CharField(256)
#     title = models.CharField(64)

#     def __str__(self):
#         return f"TITLE: {self.title}, NAME: {self.name}, SURNAME: {self.surname}" 