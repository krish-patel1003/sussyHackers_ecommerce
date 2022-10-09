from email.policy import default
from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique = True)
    first_name = models.CharField(_("first name"), max_length = 30, blank = True)
    last_name = models.CharField(_("last name"), max_length = 30, blank = True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add = True)
    is_active = models.BooleanField(_("active"), default = True)
    is_staff = models.BooleanField(_("staff"), default=False)

    # defines the user manager class for User
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []    

    class Meta:
        verbose_name = "user" 
        verbose_name_plural = "users"

    def get_full_name(self):
        # returns first name + last name
        full_name = f'{self.first_name} {self.last_name}'
        return full_name


class Category(models.Model):
    category_name = models.CharField(_("category name"), max_length = 255)

    def __str__(self):
        return f"{self.category_name}"

        
class Product(models.Model):
    product_name = models.CharField(_("product name"), max_length = 255)
    product_image = models.ImageField(default='default.jpg', upload_to='product_imgs')
    product_desc = models.TextField(_("product description"))
    product_price = models.DecimalField(_("product price"), decimal_places = 2, max_digits=8)
    product_brand = models.CharField(_("product brand"), max_length = 255)
    prodcut_category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id}: {self.product_name}"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.user}'s cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cart}: {self.product}"