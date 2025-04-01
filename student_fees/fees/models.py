from django.db import models

# # Create your models here.
from django.db import models

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     course = models.CharField(max_length=100)
#     total_fees = models.DecimalField(max_digits=10, decimal_places=2)
#     fees_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

#     @property
#     def fees_due(self):
#         return self.total_fees - self.fees_paid

#     def __str__(self):
#         return self.name



# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     course = models.CharField(max_length=100)
#     total_fees = models.DecimalField(max_digits=10, decimal_places=2)
#     fees_paid = models.DecimalField(max_digits=10, decimal_places=2)
    
#     # @property
#     def fees_due(self):
#         return self.total_fees - self.fees_paid

#     def __str__(self):
#         return self.name


# class Student(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     course = models.CharField(max_length=100)
#     total_fees = models.DecimalField(max_digits=10, decimal_places=2)
#     fees_paid = models.DecimalField(max_digits=10, decimal_places=2)

#     @property
#     def fees_due(self):
#         return self.total_fees - self.fees_paid

#     @fees_due.setter
#     def fees_due(self, value):
#         self.fees_paid = self.total_fees - value



from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    total_fees = models.DecimalField(max_digits=10, decimal_places=2)
    fees_paid = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def fees_due(self):
        return self.total_fees - self.fees_paid

    def update_fees_paid(self, new_fees_paid):
        """Update the amount of fees paid while ensuring it doesn't exceed total fees."""
        if new_fees_paid > self.total_fees:
            raise ValueError("Fees paid cannot exceed total fees.")
        self.fees_paid = new_fees_paid
        self.save()
