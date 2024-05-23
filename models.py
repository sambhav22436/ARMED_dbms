from django.db import models


from django.utils import timezone


class Admin(models.Model):
    admin_id = models.IntegerField(primary_key=True)
    admin_name = models.CharField(max_length=25)
    admin_password = models.CharField(max_length=25)
    admin_pos = models.CharField(max_length=25)
    class Meta:
      
        db_table = 'admin'

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=25)
    product_price = models.IntegerField()
    product_stockamount = models.IntegerField()
    category = models.CharField(max_length=25)
    class Meta:
        # Specify the correct table name
       db_table = 'product'


#
class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=25)
    customer_email = models.CharField(max_length=25, unique=True)
    customer_address = models.CharField(max_length=250)
    customer_phone = models.CharField(max_length=25)

    password = models.CharField(max_length=128)  # Store hashed password
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(default=timezone.now)



    class Meta:
        db_table= 'customer'



class Manufacturer(models.Model):
    manufacturer_id = models.IntegerField(primary_key=True)
    manufacturer_name = models.CharField(max_length=25)
    phone_no = models.CharField(max_length=10)

class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    rating = models.IntegerField()
    comments = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    support_rep_id = models.IntegerField()
    support_reply = models.CharField(max_length=200)

    class Meta:
        db_table='review'

class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_date = models.DateField()
    order_amount = models.IntegerField()
    tracking = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table='orders'

class OrderDetails(models.Model):
    order_detail_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_amount = models.IntegerField()

    class Meta:
        db_table='order_details'

class Cart(models.Model):
    cart_entry_id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_amount = models.IntegerField()

    class Meta:
        db_table= 'cart'

class Payment(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    payment_date = models.DateField()
    type_payment = models.CharField(max_length=30)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)

    class Meta:
        db_table='payment'

class CustomerSupport(models.Model):
    cs_id = models.IntegerField(primary_key=True)
    cs_name = models.CharField(max_length=30)
    cs_password = models.CharField(max_length=30)



from django.contrib.auth.models import User

# accounts/models.py
from django.contrib.auth.models import User
from django.db import models




# forms.py
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    # Add any other fields as needed


# views.py

