from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
    


class Shelf(models.Model):
    number = models.IntegerField()
    corridor = models.IntegerField()

    def __str__(self):
        return f"corridor: {self.corridor}  , Shelf:  {self.number}"

class book(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    publishers = models.CharField(max_length=70)
    isbn = models.CharField(max_length=13)
    language = models.CharField(max_length=30)
    shelf = models.ForeignKey(Shelf,on_delete=models.DO_NOTHING)
    author = models.ManyToManyField(Author)

    
    def __str__(self):
        return f" {self.title} "


