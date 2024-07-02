# from django.db import models
# # from django.contrib.auth.models import Group
# from django.contrib.auth.models import User

# # Create the groups
# # admin_group, created = Group.objects.get_or_create(name='Admin')
# # manager_group, created = Group.objects.get_or_create(name='Manager')
# # accountant_group, created = Group.objects.get_or_create(name='Accountant')


# class Company(models.Model):
#     company_name = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.company_name
    
# class Transaction(models.Model):
#     date = models.CharField(max_length=100)
#     description = models.CharField(max_length=255)
#     main_category = models.CharField(max_length=100)
#     sub_category = models.CharField(max_length=100)
#     receipts = models.DecimalField(max_digits=10, decimal_places=2)
#     currency = models.CharField(max_length=10, default=0)
#     payments = models.DecimalField(max_digits=10, decimal_places=2)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     file = models.FileField(upload_to='uploads/', null=True, blank=True)
#     approved = models.BooleanField(default=False)  # Approval status
#     manager_approval = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions_to_approve')
#     manager_comments = models.TextField(null=True, blank=True)


#     def __str__(self):
#         return f"{self.date} - {self.description}"




from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.company_name

class Transaction(models.Model):
    date = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    main_category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    receipts = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default=0)
    payments = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    approved = models.BooleanField(default=False)  # Approval status
    manager_approval = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions_to_approve')
    approval_status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    manager_comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.date} - {self.description}"
