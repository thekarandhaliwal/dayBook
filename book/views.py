# from django.shortcuts import render
# # from django.core.files.storage import FileSystemStorage
# from django.shortcuts import render, redirect, get_object_or_404
# # from django.contrib.auth import authenticate, login, logout
# # from django.contrib.auth import authenticate, login as auth_login
# from .forms import TransactionForm
# from django.db.models import Sum
# from django.contrib.auth.decorators import login_required



# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.auth.models import User, Group
# from .models import Transaction, Company

# @login_required
# @user_passes_test(lambda u: u.groups.filter(name='Admin').exists())
# def admin_dashboard(request):
#     # Admin-specific logic
#     return render(request, 'admin_dashboard.html')

# @login_required
# @user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
# def manager_dashboard(request):
#     # Manager-specific logic
#     return render(request, 'manager_dashboard.html')

# @login_required
# @user_passes_test(lambda u: u.groups.filter(name='Accountant').exists())
# def accountant_dashboard(request):
#     # Accountant-specific logic
#     return render(request, 'accountant_dashboard.html')



# # @login_required(login_url='login')
# # def index(request):
# #     return render(request, 'dashboard.html')

# @login_required(login_url='login')
# def index(request):
#     total_receipts = Transaction.objects.aggregate(Sum('receipts'))['receipts__sum'] or 0
#     total_payments = Transaction.objects.aggregate(Sum('payments'))['payments__sum'] or 0
    
#     context = {
#         'total_receipts': total_receipts,
#         'total_payments': total_payments
#     }
#     return render(request, 'dashboard.html', context)

# @login_required(login_url='login')
# def create_entry(request):
#     if request.method == 'POST':
#         form = TransactionForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('create_entry')
#     else:
#         form = TransactionForm()

#     context = {
#         'form': form,
#         'companies': Company.objects.all()  
#     }

#     return render(request, 'create_entry.html', context)

# def transaction_list(request):
#     transactions = Transaction.objects.all()
#     return render(request, 'transaction_list.html', {'transactions': transactions})

# @login_required(login_url='login')
# @user_passes_test(lambda u: u.groups.filter(name='Accountant').exists())
# def send_for_approval(request, pk):
#     transaction = get_object_or_404(Transaction, pk=pk)
    
#     if request.method == 'POST':
#         manager_group = Group.objects.get(name='Manager')
#         manager = manager_group.user_set.first()  # Assuming the first user in the Manager group is the manager
#         # Logic to set transaction for approval (not fully implemented here)
#         transaction.approved = False  # Initially set to False
#         transaction.manager_approval = None  # Clear manager approval if already set
#         transaction.save()
        
#         # Redirect to transaction list or wherever appropriate
#         return redirect('transaction_list')

#     # Handle GET requests if needed

#     return redirect('transaction_list')  # Default behavior after POST

# @login_required(login_url='login')
# def edit_transaction(request, pk):
#     transaction = get_object_or_404(Transaction, pk=pk)
#     if request.method == 'POST':
#         form = TransactionForm(request.POST, request.FILES, instance=transaction)
#         if form.is_valid():
#             form.save()
#             return redirect('transaction_list')
#     else:
#         form = TransactionForm(instance=transaction)

#     return render(request, 'edit_transaction.html', {'form': form})

# @login_required(login_url='login')
# def delete_transaction(request, pk):
#     transaction = get_object_or_404(Transaction, pk=pk)
#     if request.method == 'POST':
#         transaction.delete()
#         return redirect('transaction_list')
    
#     return render(request, 'delete_transaction.html', {'transaction': transaction})


# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.auth.models import User, Group
# from .models import Transaction, Company
# from .forms import TransactionForm
# from django.db.models import Sum


# @login_required(login_url='login')
# @user_passes_test(lambda u: u.groups.filter(name='Admin').exists())
# def admin_dashboard(request):
#     # Admin-specific logic (if any)
#     return render(request, 'admin_dashboard.html')

# @login_required(login_url='login')
# @user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
# def manager_dashboard(request):
#     transactions = Transaction.objects.all()
#     return render(request, 'manager_dashboard.html', {'transactions': transactions})

# @login_required(login_url='login')
# @user_passes_test(lambda u: u.groups.filter(name='Accountant').exists())
# def accountant_dashboard(request):
#     transactions = Transaction.objects.all()
#     return render(request, 'accountant_dashboard.html', {'transactions': transactions})



# # views.py

# from django.contrib.auth import authenticate, login as auth_login
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             auth_login(request, user)
#             if user.groups.filter(name='Admin').exists():
#                 return redirect('admin_dashboard')
#             elif user.groups.filter(name='Manager').exists():
#                 return redirect('manager_dashboard')
#             elif user.groups.filter(name='Accountant').exists():
#                 return redirect('accountant_dashboard')
#             else:
#                 # Handle other roles or fallback
#                 return redirect('/')
#         else:
#             # Handle invalid login
#             return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
#     else:
#         return render(request, 'registration/login.html')



# @login_required(login_url='login')
# def index(request):
#     total_receipts = Transaction.objects.aggregate(Sum('receipts'))['receipts__sum'] or 0
#     total_payments = Transaction.objects.aggregate(Sum('payments'))['payments__sum'] or 0
#     context = {
#         'total_receipts': total_receipts,
#         'total_payments': total_payments
#     }
#     return render(request, 'dashboard.html', context)

# @login_required(login_url='login')
# def create_entry(request):
#     if request.method == 'POST':
#         form = TransactionForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('create_entry')
#     else:
#         form = TransactionForm()
#     context = {
#         'form': form,
#         'companies': Company.objects.all()
#     }
#     return render(request, 'create_entry.html', context)


# @login_required(login_url='login')
# def transaction_list(request):
#     transactions = Transaction.objects.all()
#     return render(request, 'transaction_list.html', {'transactions': transactions})

# @login_required(login_url='login')
# @user_passes_test(lambda u: u.groups.filter(name='Accountant').exists())
# def send_for_approval(request, pk):
#     transaction = get_object_or_404(Transaction, pk=pk)
#     if request.method == 'POST':
#         # Assuming the manager to notify is the first user in the Manager group
#         manager_group = Group.objects.get(name='Manager')
#         manager = manager_group.user_set.first()
#         # Logic to set transaction for approval
#         transaction.approved = False  # Initial approval status
#         transaction.manager_approval = manager  # Assign the manager for approval
#         transaction.save()
#         return redirect('transaction_list')
#     return redirect('transaction_list')


# @login_required(login_url='login')
# @user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
# def approve_transaction(request, pk):
#     transaction = get_object_or_404(Transaction, pk=pk)
#     if request.method == 'POST':
#         action = request.POST.get('action')
#         comments = request.POST.get('comments', '')
#         if action == 'approve':
#             transaction.approval_status = 'Approved'
#         elif action == 'reject':
#             transaction.approval_status = 'Rejected'
#         transaction.manager_comments = comments
#         transaction.save()
#         return redirect('manager_dashboard')
#     return render(request, 'approve_transaction.html', {'transaction': transaction})


# @login_required(login_url='login')
# def edit_transaction(request, pk):
#     transaction = get_object_or_404(Transaction, pk=pk)
#     if request.method == 'POST':
#         form = TransactionForm(request.POST, request.FILES, instance=transaction)
#         if form.is_valid():
#             form.save()
#             return redirect('transaction_list')
#     else:
#         form = TransactionForm(instance=transaction)
#     return render(request, 'edit_transaction.html', {'form': form})

# @login_required(login_url='login')
# def delete_transaction(request, pk):
#     transaction = get_object_or_404(Transaction, pk=pk)
#     if request.method == 'POST':
#         transaction.delete()
#         return redirect('transaction_list')
#     return render(request, 'delete_transaction.html', {'transaction': transaction})



# from django.contrib.auth import authenticate, login as auth_login
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.auth.models import User, Group
# from django.db.models import Sum
# from .models import Transaction, Company
# from .forms import TransactionForm
# from django.contrib.auth.decorators import login_required, user_passes_test


# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             auth_login(request, user)
#             if user.groups.filter(name='Admin').exists():
#                 return redirect('admin_dashboard')
#             elif user.groups.filter(name='Manager').exists():
#                 return redirect('manager_dashboard')
#             elif user.groups.filter(name='Accountant').exists():
#                 return redirect('accountant_dashboard')
#             else:
#                 return redirect('index')  # Fallback redirect
#         else:
#             return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
#     else:
#         return render(request, 'registration/login.html')

# @login_required(login_url='login')
# def index(request):
#     total_receipts = Transaction.objects.aggregate(Sum('receipts'))['receipts__sum'] or 0
#     total_payments = Transaction.objects.aggregate(Sum('payments'))['payments__sum'] or 0
#     context = {
#         'total_receipts': total_receipts,
#         'total_payments': total_payments
#     }
#     return render(request, 'dashboard.html', context)

# @login_required(login_url='login')
# @user_passes_test(lambda u: u.groups.filter(name='Admin').exists())
# def admin_dashboard(request):
#     # Admin-specific logic (if any)
#     return render(request, 'admin_dashboard.html')

# @login_required(login_url='login')
# @user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
# def manager_dashboard(request):
#     transactions = Transaction.objects.all()
#     return render(request, 'manager_dashboard.html', {'transactions': transactions})

# # @login_required(login_url='login')
# # @user_passes_test(lambda u: u.groups.filter(name='Accountant').exists())
# # def accountant_dashboard(request):
# #     transactions = Transaction.objects.all()
# #     return render(request, 'accountant_dashboard.html', {'transactions': transactions})
# @login_required(login_url='login')
# @user_passes_test(lambda u: u.groups.filter(name='Accountant').exists())
# def accountant_dashboard(request):
#     transactions = Transaction.objects.all()
#     return render(request, 'accountant_dashboard.html', {'transactions': transactions})


# @login_required(login_url='login')
# def create_entry(request):
#     if request.method == 'POST':
#         form = TransactionForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('create_entry')
#     else:
#         form = TransactionForm()
#     context = {
#         'form': form,
#         'companies': Company.objects.all()
#     }
#     return render(request, 'create_entry.html', context)

# # @login_required(login_url='login')
# # def transaction_list(request):
# #     transactions = Transaction.objects.all()
# #     return render(request, 'transaction_list.html', {'transactions': transactions})

# # @login_required(login_url='login')
# # @user_passes_test(lambda u: u.groups.filter(name='Accountant').exists())
# # def transaction_list(request):
# #     transactions = Transaction.objects.all()  # Or filter based on specific criteria
# #     return render(request, 'transaction_list.html', {'transactions': transactions})

# from django.http import HttpResponse
# import logging
# logger = logging.getLogger(__name__)

# # @login_required(login_url='login')
# # def transaction_list(request):
    
# #     if request.user.is_authenticated:
# #         if request.user.groups.filter(name='Accountant').exists():
# #             transactions = Transaction.objects.all()
# #             return render(request, 'transaction_list.html', {'transactions': transactions})
# #         else:
# #             return HttpResponse("You are not in the Accountant group.")
# #     else:
# #         return HttpResponse("You are not authenticated.")
# import logging

# logger = logging.getLogger(__name__)

# @login_required(login_url='login')
# @user_passes_test(lambda u: u.groups.filter(name='Accountant').exists(), login_url='login')
# def transaction_list(request):
#     user_groups = request.user.groups.all()
#     logger.info(f"User: {request.user.username}, Groups: {[group.name for group in user_groups]}")
#     is_accountant = request.user.groups.filter(name='Accountant').exists()
#     logger.info(f"User: {request.user.username}, is_accountant: {is_accountant}")
#     if not is_accountant:
#         return HttpResponse("You are not in the Accountant group.", status=403)

#     transactions = Transaction.objects.all()
#     return render(request, 'transaction_list.html', {'transactions': transactions})


# @login_required(login_url='login')
# @user_passes_test(lambda u: u.groups.filter(name='Accountant').exists())
# def send_for_approval(request, pk):
#     transaction = get_object_or_404(Transaction, pk=pk)
#     if request.method == 'POST':
#         # Assuming the manager to notify is the first user in the Manager group
#         manager_group = Group.objects.get(name='Manager')
#         manager = manager_group.user_set.first()
#         # Logic to set transaction for approval
#         transaction.approved = False  # Initial approval status
#         transaction.manager_approval = manager  # Assign the manager for approval
#         transaction.save()
#         return redirect('transaction_list')
#     return redirect('transaction_list')

# @login_required(login_url='login')
# @user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
# def approve_transaction(request, pk):
#     transaction = get_object_or_404(Transaction, pk=pk)
#     if request.method == 'POST':
#         action = request.POST.get('action')
#         comments = request.POST.get('comments', '')
#         if action == 'approve':
#             transaction.approval_status = 'Approved'
#         elif action == 'reject':
#             transaction.approval_status = 'Rejected'
#         transaction.manager_comments = comments
#         transaction.save()
#         return redirect('manager_dashboard')
#     return render(request, 'approve_transaction.html', {'transaction': transaction})

# @login_required(login_url='login')
# def edit_transaction(request, pk):
#     transaction = get_object_or_404(Transaction, pk=pk)
#     if request.method == 'POST':
#         form = TransactionForm(request.POST, request.FILES, instance=transaction)
#         if form.is_valid():
#             form.save()
#             return redirect('transaction_list')
#     else:
#         form = TransactionForm(instance=transaction)
#     return render(request, 'edit_transaction.html', {'form': form})

# @login_required(login_url='login')
# def delete_transaction(request, pk):
#     transaction = get_object_or_404(Transaction, pk=pk)
#     if request.method == 'POST':
#         transaction.delete()
#         return redirect('transaction_list')
#     return render(request, 'delete_transaction.html', {'transaction': transaction})



from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.db.models import Sum
from .models import Transaction, Company
from .forms import TransactionForm
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            if user.groups.filter(name='Admin').exists():
                return redirect('admin_dashboard')
            elif user.groups.filter(name='Manager').exists():
                return redirect('manager_dashboard')
            elif user.groups.filter(name='Accountant').exists():
                return redirect('accountant_dashboard')
            else:
                return redirect('index')  # Fallback redirect
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'registration/login.html')

@login_required(login_url='login')
def index(request):
    total_receipts = Transaction.objects.aggregate(Sum('receipts'))['receipts__sum'] or 0
    total_payments = Transaction.objects.aggregate(Sum('payments'))['payments__sum'] or 0
    context = {
        'total_receipts': total_receipts,
        'total_payments': total_payments
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.groups.filter(name='Admin').exists())
def admin_dashboard(request):
    # Admin-specific logic (if any)
    return render(request, 'admin_dashboard.html')

# @login_required(login_url='login')
# @user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
# def manager_dashboard(request):
#     transactions = Transaction.objects.all()
#     return render(request, 'manager_dashboard.html', {'transactions': transactions})


# import logging

# logger = logging.getLogger(__name__)

# @login_required(login_url='login')
# @user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
# def manager_dashboard(request):
#     logger.debug(f"User: {request.user.username}, Manager Dashboard accessed.")
#     transactions = Transaction.objects.all()
#     logger.debug(f"Transactions fetched: {transactions}")
#     return render(request, 'manager_dashboard.html', {'transactions': transactions})

import logging

logger = logging.getLogger(__name__)

@login_required(login_url='login')
@user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
def manager_dashboard(request):
    logger.info(f"User: {request.user.username}, Groups: {request.user.groups.all()}")
    transactions_for_approval = Transaction.objects.filter(approved=False)
    return render(request, 'manager_dashboard.html', {'transactions_for_approval': transactions_for_approval})


@login_required(login_url='login')
@user_passes_test(lambda u: u.groups.filter(name='Accountant').exists())
def accountant_dashboard(request):
    transactions = Transaction.objects.all()
    return render(request, 'accountant_dashboard.html', {'transactions': transactions})

@login_required(login_url='login')
def create_entry(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_entry')
    else:
        form = TransactionForm()
    context = {
        'form': form,
        'companies': Company.objects.all()
    }
    return render(request, 'create_entry.html', context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.groups.filter(name='Accountant').exists())
def send_for_approval(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        # Assuming the manager to notify is the first user in the Manager group
        manager_group = Group.objects.get(name='Manager')
        manager = manager_group.user_set.first()
        # Logic to set transaction for approval
        transaction.approved = False  # Initial approval status
        transaction.manager_approval = manager  # Assign the manager for approval
        transaction.save()
        return redirect('transaction_list')
    return redirect('transaction_list')

@login_required(login_url='login')
@user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
def approve_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        action = request.POST.get('action')
        comments = request.POST.get('comments', '')
        if action == 'approve':
            transaction.approval_status = 'Approved'
        elif action == 'reject':
            transaction.approval_status = 'Rejected'
        transaction.manager_comments = comments
        transaction.save()
        return redirect('manager_dashboard')
    return render(request, 'approve_transaction.html', {'transaction': transaction})

@login_required(login_url='login')
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, request.FILES, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'edit_transaction.html', {'form': form})

@login_required(login_url='login')
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'delete_transaction.html', {'transaction': transaction})

@login_required(login_url='login')
@user_passes_test(lambda u: u.groups.filter(name='Accountant').exists())
def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})
