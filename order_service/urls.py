from django.contrib import admin
from django.urls import path
from orders.views import OrderListCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', OrderListCreate.as_view()),
]
