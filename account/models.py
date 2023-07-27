from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, name,phone_number, password=None,password2=None,**extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """

        if not email:
            raise ValueError("Users must have an email address")
        if not phone_number:
            raise ValueError("Users must have a phone number")

        user = self.model(
         
            email=self.normalize_email(email),
            name=name,
            phone_number=phone_number,
           **extra_fields
        )


        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,phone_number,name, password=None, password2=None,**extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """

         
        user = self.create_user(
            email,
            name=name,
            phone_number=phone_number,
            password=password,
            **extra_fields

        )
 
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    name=models.CharField(max_length=100)
    phone_number=models.IntegerField(unique=True)
    password2=models.CharField(max_length=30, null=True)
    photo = models.ImageField(upload_to='profile_photos', blank=True, null=True,max_length=500)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at=models.DateTimeField( auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects=UserManager()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["name",'email']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
# Create your models here.
