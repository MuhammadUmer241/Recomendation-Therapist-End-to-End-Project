from django.db import models

class Therapist(models.Model):
    # User information
    name = models.CharField(max_length=255)  # User's name
    age = models.IntegerField()  # User's age
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    user_gender = models.CharField(max_length=6, choices=GENDER_CHOICES)  # User's gender (Male, Female, Other)
    
    # Reason for therapy
    therapy_issues = models.TextField()  # What brings the user to therapy?

    # Therapy approach (choices based on your preferences)
    therapy_approaches = models.TextField()  # This can be a comma-separated string or JSON format

    # Budget
    budget = models.IntegerField()  # User's budget for therapy

    # Availability (choices for availability, e.g., morning, afternoon, etc.)
    AVAILABILITY_CHOICES = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
        ('Flexible', 'Flexible'),
    ]
    availability = models.CharField(max_length=10, choices=AVAILABILITY_CHOICES)  # User's availability preference
    
    # Therapist gender preference
    therapist_gender = models.CharField(max_length=6, choices=GENDER_CHOICES)  # Gender preference for therapist

    def __str__(self):
        return f"{self.name} - {self.user_gender}"

    class Meta:
        verbose_name = 'Therapist Recommendation'
        verbose_name_plural = 'Therapist Recommendations'
