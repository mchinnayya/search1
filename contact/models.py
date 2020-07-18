from django.db import models

from branch.models import Branch


class Contact(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    extension_status = models.SmallIntegerField(default=0)  # 0 is not activate 1 is activate
    contact_name = models.CharField(max_length=255)
    extension_number = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    # def __str__(self):
    #     return self.contact_name+self.extension_number
