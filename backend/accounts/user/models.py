from django.db import models

class UserInfo(models.Model):
    # ID, PW, RE PW, Name, Birth, Email, Phone Number, API KEY, SEC KEY
    user_id = models.CharField(max_length= 100, unique= True)
    password = models.CharField(max_length = 100)
    re_password = models.CharField(max_length= 100)
    user_name = models.CharField(max_length= 100)
    birth = models.CharField(max_length= 100)
    email = models.CharField(max_length= 100)
    phone_number = models.CharField(max_length= 100)
    api_key = models.CharField(max_length= 100)
    sec_key = models.CharField(max_length= 100)
    # user_id, password, re_password, user_name, birth, email, phone_number, api_key, sec_key

    date = models.DateTimeField()