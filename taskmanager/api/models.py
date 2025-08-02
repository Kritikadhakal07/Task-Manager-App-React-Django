from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    #When someone prints a Task object 
    # (or sees it in the admin panel), 
    # show the title instead of a default object
    #  representation like <Task object (1)>
    def __str__(self):
        return self.title
    


