
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from book.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('', user_login, name="user_login"),
    path('', index, name="index"),
    path('create_entry/', create_entry, name="create_entry"),
    path('transactions/', transaction_list, name='transaction_list'),
    path('edit/<int:pk>/', edit_transaction, name='edit_transaction'),
    path('delete/<int:pk>/', delete_transaction, name='delete_transaction'),
    path('send-for-approval/<int:pk>/', send_for_approval, name='send_for_approval'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

