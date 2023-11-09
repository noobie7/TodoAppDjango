from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("To Do", "To Do"),
            ("In Progress", "In Progress"),
            ("Done", "Done"),
        ],
        default="To Do"
    )

    def __str__(self):
        return self.title
