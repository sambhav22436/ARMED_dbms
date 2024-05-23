# views.py

from django.shortcuts import render
from django.http import JsonResponse



from .models import Admin, Product, Manufacturer, Review, Orders, OrderDetails, Cart, Payment, CustomerSupport,Customer

def admin_list(request):
    admins = Admin.objects.all()
    return render(request, 'admin_list.html')

def product_list(request):
    products = Product.objects.all()
    
    return render(request, 'product.html', {'products': products})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, 'manufacturer_list.html', {'manufacturers': manufacturers})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

def orders_list(request):
    orders = Orders.objects.all()
    return render(request, 'orders_list.html', {'orders': orders})

def order_details_list(request):
    order_details = OrderDetails.objects.all()
    return render(request, 'order_details_list.html', {'order_details': order_details})

def cart_list(request):
    carts = Cart.objects.all()
    return render(request, 'cart_list.html', {'carts': carts})

def payment_list(request):
    return render(request, 'payments.html')

def customer_support_list(request):
    customer_supports = CustomerSupport.objects.all()
    return render(request, 'customer_support_list.html', {'customer_supports': customer_supports})


from django.db import connection


from django.db import connection
from django.shortcuts import render

def custom_query(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT product_name, product_stockamount FROM product")
        rows = cursor.fetchall()
    
    return render(request, 'custom_query_result.html', {'rows': rows})

from django.shortcuts import render, redirect
from django.db import connection

from django.contrib.auth import login, authenticate


from django.shortcuts import render, redirect
from .models import Admin  # Assuming Admin model is defined in models.py


def admin_login(request):
    if request.method == 'POST':
        admin_name = request.POST.get('admin_name')
        admin_password = request.POST.get('admin_password')
        
        try:
            admin = Admin.objects.get(admin_name=admin_name)
        except Admin.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

        if admin.admin_password == admin_password:
            # Authentication successful
            # You may want to add additional checks here if needed
            # For example, checking if the user is active or banned
            # Then set the session or any other logic you require
            return redirect('admin_dashboard.html')  # Redirect to admin dashboard or any other page
        else:
            # Invalid password
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    # If it's a GET request or login failed, render the login page
    return render(request, 'login.html')




from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def login_view(request):
    if request.method =='GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        
        # Debug: Print received form data
        logger.debug(f"Received login request - Username: {username}, Password: {password}")
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Debug: Print successful authentication
            logger.debug("Authentication successful")
            
            # Login the user
            login(request, user)
            
            # Debug: Print user information
            logger.debug(f"User logged in - Username: {user.username}, Email: {user.email}")
            
            # Redirect to a success page
            return redirect('product_list')
        else:
            # Debug: Print invalid login attempt
            logger.debug("Invalid login attempt")
            
            # Return an invalid login error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

from django.shortcuts import render
from .models import Product  # Assuming you have a Product model defined in your models.py file



def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, product_id):
    # Retrieve the product object from the database
    product = get_object_or_404(Product, pk=product_id)
    
    # Render the product detail template with the product object
    return render(request, 'product_detail.html', {'product': product})



from django.shortcuts import render, redirect
from .models import Product, Cart,Customer

from django.db import connection

def add_to_cart(request, product_id):
    # Retrieve the current user
    user = request.user

    cust= Customer.objects.get(customer_email=user)
    
    # Retrieve the product object from the database
    product = Product.objects.get(pk=product_id)
    
    # Check if the product is already in the user's cart
    
    # If the product is not in the cart, insert it into the CART table using SQL
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO CART (QUANTITY, CUSTOMER_ID, PRODUCT_ID, TOTAL_AMOUNT)
            VALUES (%s, %s, %s, %s)
        """, [1, cust.customer_id, product_id, product.product_price])
 
    
    # Redirect the user to the product detail page
    return redirect('product_list')

    
    
    
    
from django.shortcuts import render
from .models import Product

# views.py
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Create a new user object
            user = User.objects.create_user(username=username, email=email, password=password)
            # Optionally, you can log in the user after registration
            # login(request, user)
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



from django.shortcuts import render
from .models import Cart

def cart_view(request):
    # Retrieve the current user
    user = request.user
    cust= Customer.objects.get(customer_email=user)


    # Retrieve cart items for the current user
    cart_items = Cart.objects.filter(customer=cust)

    # Calculate total amount
    total_amount = sum(item.total_amount for item in cart_items)

    # Pass cart items and total amount to the cart page template
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_amount': total_amount})


def checkout(request):
    # Retrieve the current user
    user = request.user
    cust= Customer.objects.get(customer_email=user)


    # Retrieve cart items for the current user
    cart_items = Cart.objects.filter(customer=cust)

    # Calculate total amount
    total_amount = sum(item.total_amount for item in cart_items)

    # Pass cart items and total amount to the cart page template
    return render(request, 'checkout.html', {'cust': cust, 'total_amount': total_amount})






from django.shortcuts import render
from django.http import HttpResponse
from .models import Payment, Orders, OrderDetails
import random
from datetime import date

def paymentp(request):
    if request.method == 'POST':
        # Process form submission
        # For simplicity, let's assume the order_id is generated earlier and passed as a hidden input field in the form
        user=request.user
        cust= Customer.objects.get(customer_email=user)
        cart_items = Cart.objects.filter(customer=cust)

    # Calculate total amount
        total_amount = sum(item.total_amount for item in cart_items)
        # Generate fake transaction ID and tracking ID
        transaction_id = random.randint(100000, 999999)
        tracking_id = random.randint(100000, 999999)
        order_id = random.randint(100000, 999999)


          

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO ORDERS (ORDER_ID, ORDER_DATE, ORDER_AMOUNT, TRACKING, CUSTOMER_ID)
                VALUES (%s, %s, %s, %s, %s)
            """, [order_id, date.today(), total_amount , tracking_id, cust.customer_id])

        for item in cart_items:  # Assuming 'items' is a list of tuples containing product_id, quantity, and total_amount
                
                with connection.cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO ORDER_DETAILS (ORDER_ID, PRODUCT_ID, QUANTITY, TOTAL_AMOUNT)
                        VALUES (%s, %s, %s, %s)
                    """, [order_id, item.product.product_id, item.quantity, item.product.product_price * item.quantity])

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO PAYMENT (TRANSACTION_ID, PAYMENT_DATE, TYPE_PAYMENT, ORDER_ID)
                VALUES (%s, %s, %s, %s)
            """, [transaction_id, date.today(), "cash" , order_id])
        
        with connection.cursor() as cursor:
         cursor.execute("""
            DELETE FROM CART
            WHERE CUSTOMER_ID = %s
        """, [cust.customer_id])
        
        
        # Update the order status or any other necessary actions
        
        return redirect('product_list')
    else:
        return render(request, 'payments.html')
    





def profile(request):
    # Retrieve the current user's customer details
    customer = Customer.objects.get(customer_email=request.user)
    return render(request, 'profile.html', {'customer': customer})



from django.shortcuts import render
from .models import Orders, OrderDetails

def vd(request):
    user_id = Customer.objects.get(customer_email=request.user)
    past_orders = Orders.objects.filter(customer_id=user_id)

    context = {
        'past_orders': past_orders
    }
    return render(request, 'orderd.html', context)


from django.shortcuts import render
from .models import Review, Product

def check_reviews(request):
    # Retrieve all products
    products = Product.objects.all()
    
    # Dictionary to store reviews for each product
    product_reviews = {}
    
    # Loop through each product and retrieve its reviews
    for product in products:
        reviews = Review.objects.filter(product_id=product.product_id)
        product_reviews[product] = reviews
    
    return render(request, 'check_reviews.html', {'product_reviews': product_reviews})





from django.contrib.auth.hashers import make_password

import re

def signup(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_password = request.POST.get('customer_password')
        customer_address = request.POST.get('customer_address')
        customer_phone = request.POST.get('customer_phone')
        customer_id = random.randint(100000, 999999)

        # Email validation
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', customer_email):
            # Handle invalid email address (e.g., return an error message)
            return render(request, 'signup.html', {'error_message': 'Invalid email address'})

        # Phone number validation
        if not customer_phone.isdigit():
            # Handle non-integer phone number (e.g., return an error message)
            return render(request, 'signup.html', {'error_message': 'Phone number must contain only digits'})

        # Hash the password using Django's make_password function
        hashed_password = make_password(customer_password)

        # Insert customer details into the database using embedded SQL
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO CUSTOMER (CUSTOMER_ID,CUSTOMER_NAME, CUSTOMER_EMAIL, PASSWORD, CUSTOMER_ADDRESS, CUSTOMER_PHONE)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, [customer_id, customer_name, customer_email, customer_password, customer_address, customer_phone])

        # Create a new user instance with the email and hashed password
        new_user = User.objects.create_user(username=customer_email, email=customer_email, password=customer_password)
        new_user.save()

        # Redirect to a success page or login page
        return redirect('product_list')
    else:
        # Render the signup form page
        return render(request, 'signup.html')




def edit_profile(request):
    customer = Customer.objects.get(customer_email=request.user)
    if request.method == 'POST':
        # Get the new values from the form
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_address = request.POST.get('customer_address')
        customer_phone = request.POST.get('customer_phone')

        if customer_email != customer.customer_email:
            # Update Django username to the new email
            user = request.user
            user.username = customer_email
            user.save()

        # Check if each field has changed and update only the changed fields
        if customer_name != customer.customer_name:
            customer.customer_name = customer_name
        if customer_email != customer.customer_email:
            customer.customer_email = customer_email
        if customer_address != customer.customer_address:
            customer.customer_address = customer_address
        if customer_phone != customer.customer_phone:
            customer.customer_phone = customer_phone


        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE CUSTOMER
                SET customer_name = %s, customer_email = %s, customer_address = %s, customer_phone = %s
                WHERE customer_id = %s
            """, [customer_name, customer_email, customer_address, customer_phone, customer.customer_id])

        # Redirect to the profile page
        return redirect('profile')
    else:
        # Render the edit profile form template
        return render(request, 'profile.html')    
    





def remove_from_cart(request):
    if request.method == 'POST':
        # Get the item id from the form
        item_id = request.POST.get('item_id')

        # Remove the item from the cart
        Cart.objects.filter(cart_entry_id=item_id).delete()

        # Redirect back to the cart page
        return redirect('cart_view')



from django.shortcuts import render, redirect
from .models import Review

def submit_review(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')
        review_id= random.randint(100000, 999999)
        customer = Customer.objects.get(customer_email=request.user)
        product= Product.objects.get(product_name= product)
        # Save the review to the database
        Review.objects.create(review_id=review_id,customer_id=customer.customer_id, product_id=product.product_id, rating=rating, comments=comments)
        return redirect('vd')  # Redirect to the order details page
    else:
        return redirect('vd')  # Redirect to the order details page if not a POST request




from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie  # Import the decorator

from .models import Product

@ensure_csrf_cookie  # Decorate the view function to ensure CSRF cookie is set
def shop_by_category(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()  # Or any other default behavior if no category is selected

    return render(request, 'product.html', {'products': products})

