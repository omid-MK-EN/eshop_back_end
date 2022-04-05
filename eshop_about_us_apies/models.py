from django.db import models

class AboutUs(models.Model):
    company_name = models.CharField(max_length=50)
    email = models.EmailField()
    tel = models.CharField(max_length=30)
    fax = models.CharField(max_length=30)
    mobile =models.CharField(max_length=30)
    compane_descriptions = models.TextField()
    adress = models.TextField()
    logo = models.ImageField(upload_to = "eshop_about_us_log/")
    is_active = models.BooleanField(default=False)

    def __str__(self) :
        return self.company_name
