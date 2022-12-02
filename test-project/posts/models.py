from django.db import models


class PostModel(models.Model):
    text = models.TextField()

    def __str__(self):
        return f"{self.text[:30]}..." if len(str(self.text)) > 30 else self.text
