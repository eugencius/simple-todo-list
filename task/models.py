from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=255)
    status = models.CharField(
        max_length=1,
        default='I',
        choices=(
            ('I', 'In Progress'),
            ('F', 'Finished')
        )
    )

    def __str__(self):
        return self.task
