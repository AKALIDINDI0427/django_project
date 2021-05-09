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


# class ContactDetails(models.Model):
#     HOW_DID_YOU_HEAR_CHOICES = [(None, "--None--"),
#                                 ("internet", "Internet"),
#                                 ("friend/relative", "Friend/Relative"),
#                                 ("socialnetworking", "Social Networking"),
#                                 ("advertisement", "Advertisement")]
#
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.IntegerField()
#     project_type = models.CharField(max_length=100)
#     date = models.DateField()
#     venue = models.CharField(max_length=100)
#     budget = models.IntegerField()
#     guests_count = models.IntegerField()
#     how_did_you_hear = models.CharField(max_length=20, choices=HOW_DID_YOU_HEAR_CHOICES)
#     questions = models.TextField(max_length=250)
#
#     class Meta:
#         db_table = "contact_details"


class ContactDetailsTable(models.Model):
    HOW_DID_YOU_HEAR_CHOICES = [("None", "--None--"),
                                ("internet", "Internet"),
                                ("friend/relative", "Friend/Relative"),
                                ("socialnetworking", "Social Networking"),
                                ("advertisement", "Advertisement")]

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    project = models.CharField(max_length=100)
    date = models.DateField()
    venue = models.CharField(max_length=100)
    budget = models.IntegerField()
    guests = models.IntegerField()
    aboutme = models.CharField(max_length=17, choices=HOW_DID_YOU_HEAR_CHOICES)
    questions = models.CharField(max_length=2000)

    class Meta:
        db_table = "contact_details"

