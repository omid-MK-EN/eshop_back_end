# from django.db import models
# import datetime
# from django.db import models
#
# class ContactUs(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#     title = models.CharField(max_length=50)
#     descriptions = models.TextField()
#     is_read = models.BooleanField(default=False)
#     read_time = models.DateTimeField(blank=True,null=True)
#
#
#     def __str__(self) -> str:
#         return self.name
#
#     @property
#     def read_time(self):
#         if self.is_read:
#             return datetime.datetime.now()
#         else:
#             return None
#
# class ForwardContactUsMessage(models.Model):
#     message = models.ForeignKey(ContactUs,on_delete=models.CASCADE,related_name="forward_message")
#     title_forward = models.CharField(max_length=50,null=True,blank=True)
#     forward_message = models.TextField()
#     forward_time = models.DateTimeField(auto_now_add=datetime.datetime.now())
#
#
#     def __str__(self) -> str:
#          return self.message.name