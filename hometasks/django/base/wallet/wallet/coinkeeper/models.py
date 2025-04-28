from django.db import models
from django.conf import settings
import datetime

class Category(models.Model):
    title = models.CharField(max_length=100, null=False)
    slug = models.SlugField(max_length=100, unique=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    transaction_type = models.CharField(max_length=30, choices=TRANSACTION_TYPE_CHOICES, null=False)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0, null=False)
    created_at = models.DateTimeField(default=datetime.datetime.now, null=False)

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='transactions', null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='transactions', null=False)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(transaction_type__in=['income', 'expense']), name='check_transaction_type')
        ]

    def __str__(self):
        return f"Transaction {self.id} - {self.transaction_type} of {self.amount}"