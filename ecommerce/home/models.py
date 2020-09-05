from django.db import models

# Create your models here.
# when ever you made a change in the models
# python manage.py makemigrations
# python manage.py migrate


class HomeDetails(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    class Meta:
        db_table = "home_details"

class QuoteDetails(models.Model):
    dropdown = [
        (None, "--None--"),
        ("broad", "Broadcast"),
        ("commer", "Commercial"),
        ("corporate", "Corporate Video"),
        ("feature", "Feature Film")
    ]
    dropdown_1 = [
        ("0", "Yes"),
        ("1", "No"),
        ("2", "Maybe")
    ]
    project_type = models.CharField(max_length=100,choices=dropdown)
    availability = models.CharField(max_length=10,choices=dropdown_1)
    date = models.CharField(max_length=15)



