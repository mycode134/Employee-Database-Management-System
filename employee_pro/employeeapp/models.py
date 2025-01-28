from django.db import models


class Employee(models.Model):
    emp_name = models.CharField(
        max_length=256, null=True, blank=True, help_text="enter the employee name"
    )
    
    id = models.AutoField(primary_key=True)
    emp_id = models.IntegerField(null=True)
    emp_gender = models.CharField(max_length=20, null=True)  # Reduced length
    emp_contact = models.CharField(max_length=15, null=True)  # Changed to CharField for phone numbers
    emp_email = models.EmailField(null=True)
    emp_address = models.TextField(null=True)
    emp_department = models.CharField(max_length=100, null=True)  # Fixed typo and reduced length
    emp_jobtitle = models.CharField(max_length=100, null=True)  # Reduced length
    emp_link = models.URLField(null=True, help_text="LinkedIn or LeetCode profile")
    joined_at = models.DateTimeField(auto_now_add=True)
    emp_salary = models.FloatField(null=True)
    
    
    class Meta:  
        db_table = "employee"  