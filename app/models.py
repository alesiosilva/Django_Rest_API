from django.db import models

# Modelagem para objeto
class Todo(models.Model):
    name = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)