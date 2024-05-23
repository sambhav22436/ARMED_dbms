from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from .views import register

urlpatterns = [
    path('admin/', views.admin_list, name='admin_list'),
    path('product/', views.product_list, name='product_list'),
    path('cart/', views.cart_view, name='cart_view'),
    path('checkout/', views.checkout, name='checkout'),
    path('payments/', views.payment_list, name='payment_list'),
    path('paymentp/', views.paymentp, name='paymentp'),
    path('customer/', views.customer_list, name='customer_list'),
    path('manufacturer/', views.manufacturer_list, name='manufacturer_list'),
    path('review/', views.review_list, name='review_list'),
    path('orders/', views.orders_list, name='orders_list'),
    path('order-details/', views.order_details_list, name='order_details_list'),
    path('cart/', views.cart_list, name='cart_list'),
    path('payment/', views.payment_list, name='payment_list'),
    path('customer-support/', views.customer_support_list, name='customer_support_list'),
    path('custom-query/', views.custom_query, name='custom_query'),
#    path('product-detail/<int:product_id>/', views.order_product, name='order_product'),
#    path('order-success/', views.order_success, name='order_success'),
    path('login/', views.login_view ,name='login_view'),
    path('signup/', views.signup, name='signup'),
#    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-login/', views.admin_dashboard, name='admin_dashboard'),
    path('product-detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('profile/', views.profile ,name='profile'),
    path('orderd/', views.vd ,name='vd'),
    path('check-reviews/', views.check_reviews ,name='check_reviews'),
    path('editprofile/', views.edit_profile ,name='edit_profile'),
    path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('submit-reviews/', views.submit_review ,name='submit_review'),
    path('shop/', views.shop_by_category, name='shop_by_category'),


    path('register/', register, name='register'),
    # Other URL patterns...


]

