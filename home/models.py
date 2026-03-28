from django.db import models

# Create my models here.

# This is about model which is taking querys and feedbacks from users.
class about(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    # timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + '  ' + self.email

# This is signup model which is taking and storing users registration details.
class signup(models.Model):
    username = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    pass1 = models.CharField(max_length=20)
    pass2 = models.CharField(max_length=20)

