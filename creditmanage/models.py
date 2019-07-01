from django.db import models

class client(models.Model):
	
	name = models.CharField(max_length=200)
	uid = models.CharField(max_length=200)
	balance = models.IntegerField()

	def __str__(self):
		return self.name

	def addMoney(self , x):
		self.balance = self.balance + x

	def deductMoney(self , x):
		self.balance = self.balance - x
		
