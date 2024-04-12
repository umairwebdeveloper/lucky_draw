from django.db import models

class Voucher(models.Model):
    code = models.CharField(verbose_name='Voucher code of 6 characters' ,max_length=6, unique=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
    
class PrizeProbability(models.Model):
    # add description for money and percentage
    money = models.IntegerField(verbose_name='Money in USD', default=0)
    percentage = models.FloatField(verbose_name='Percentage probability', default=0.0)
    
    def __str__(self):
        return f'${self.money} - {self.percentage}%'
    
    class Meta:
        verbose_name = 'Prize Probability'
        verbose_name_plural = 'Prize Probabilities'

class WinGiftEmail(models.Model):
    email = models.EmailField()
    prize_won = models.IntegerField(verbose_name='Prize money won',  default=0)
    number_selected = models.IntegerField(verbose_name='Box number selected', default=0)
    voucher = models.ForeignKey(Voucher, verbose_name='A unique voucher number entered', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
