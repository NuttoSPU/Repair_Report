from django.db import models

# Create your models here.
    
class Report(models.Model):
    Status_Choice = [
        ('Waiting','รอดำเนินการ'),
        ('In Progress','กำลังดำเนินการ'),
        ('Fixed','ซ่อมแล้ว')
    ]

    Topic = models.CharField(max_length=250)
    Department = models.CharField(max_length=250)
    User = models.CharField(max_length=100)
    Computer_Equipment = models.CharField(max_length=250)
    Details = models.CharField(max_length=1000)
    Status = models.CharField(max_length=13,choices=Status_Choice,default='Waiting')
    Date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.Topic}-{self.Department}-{self.User}-{self.Computer_Equipment}-{self.Details}-{self.Status}-{self.Date}'