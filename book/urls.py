
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from book.views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('manager/dashboard/', manager_dashboard, name='manager_dashboard'),
    path('accountant/dashboard/', accountant_dashboard, name='accountant_dashboard'),
    path('', index, name='index'),
    path('create_entry/', create_entry, name='create_entry'),
    path('transactions/', transaction_list, name='transaction_list'),
    path('send-for-approval/<int:pk>/', send_for_approval, name='send_for_approval'),
    path('approve/<int:pk>/', approve_transaction, name='approve_transaction'),
    path('edit/<int:pk>/', edit_transaction, name='edit_transaction'),
    path('delete/<int:pk>/', delete_transaction, name='delete_transaction'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

