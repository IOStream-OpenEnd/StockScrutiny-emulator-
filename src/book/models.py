from django.db import models

# Create your models here.
class Client(models.Model):
    user_name = models.CharField(max_length = 200, primary_key = True)
    password = models.CharField(max_length = 32)
    email_user = models.EmailField(unique = True)

    def __str__(self):
        return '%s %s' %(self.user_name, self.email_user)

class Log(models.Model):
    user_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_no = models.CharField(max_length = 10, unique = True, primary_key = True)
    share_name = models.CharField(max_length = 30)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=3)
    mode = models.CharField(max_length = 4)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user_name', 'order_no'),)

    def __str__(self):
        return self.order_no

class Wallet(models.Model):
    user_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=3)