from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    """Custom user manager where email is the unique identifier instead of username."""

    def create_user(self, email, password=None, **extra_fields):
        """Creates and returns a regular user with the given email and password."""
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and returns a superuser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    """Custom User model that uses email as the unique identifier."""
    
    username = None  # Remove username field
    email = models.EmailField(unique=True)  # Email as unique identifier

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",  # Fix reverse accessor clash
        blank=True
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",  # Fix reverse accessor clash
        blank=True
    )

    objects = CustomUserManager()  # Use the custom manager

    USERNAME_FIELD = "email"  # Authenticate using email
    REQUIRED_FIELDS = []  # No extra required fields

    def __str__(self):
        return self.email  # Return email as string representation
