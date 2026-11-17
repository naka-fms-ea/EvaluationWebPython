from django.db import models

# Create your models here.


class User(models.Model):
    us_first_name = models.CharField(max_length=40)
    us_last_name = models.CharField(max_length=100)
    us_email = models.EmailField(max_length = 254)
    us_login = models.CharField(max_length=100)
    us_password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.us_first_name} {self.us_last_name} {self.us_email}"


class Skill(models.Model):
    sk_name = models.CharField(max_length=200)
    sk_description = models.CharField(max_length=400)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.sk_name} : {self.sk_description}"


class Activity(models.Model):
    ac_name = models.CharField(max_length=200)
    ac_description = models.CharField(max_length=400)
    ac_fk_skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ac_name} : {self.ac_description}"


class Slot(models.Model):
    sl_date = models.DateField()
    ac_fk_activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    ac_fk_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sl_date}"