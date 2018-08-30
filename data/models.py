from django.db import models

# Create your models here.


class DomainName(models.Model):
    domain_name = models.CharField(max_length=32)
    business = models.CharField(max_length=50)
    conf_file = models.CharField(max_length=32)
    upstream = models.CharField(max_length=16)


