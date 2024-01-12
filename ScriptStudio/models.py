from django.db import models

class scripts(models.Model):
    scripts_id = models.CharField(max_length = 255)
    prompt = models.CharField(max_length = 255)
    paragraph1 = models.CharField(max_length = 40000)
    paragraph2 = models.CharField(max_length = 2000)
    paragraph3 = models.CharField(max_length = 40000)
    paragraph4 = models.CharField(max_length = 40000)
    paragraph5 = models.CharField(max_length = 40000)
