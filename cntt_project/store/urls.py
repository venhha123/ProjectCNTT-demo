from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  #tránh nhầm vs view của store

app_name = 'store'
urlpatterns = [
    #store
    path('', views.store, name="store"), #url 'store:store'
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update"),
    path('<int:pID>', views.view_book_detail, name="product_detail"),#view_detail
    
    # login handle
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="store/pages/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='store:store'), name='logout'),
    
    # checkout
    path('place/', views.placeOrder, name='place'),
    path('comment/', views.comment, name='comment'),
    path('checkout_info/', views.view_checkout_info, name='checkout_info'),
    path('checkout_info/<int:iID>', views.view_checkout_detail, name='checkout_detail'),

]
