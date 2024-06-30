from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth import authenticate, login as auth_login
from .forms import TransactionForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required



from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from .models import Transaction, Company

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Admin').exists())
def admin_dashboard(request):
    # Admin-specific logic
    return render(request, 'admin_dashboard.html')

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
def manager_dashboard(request):
    # Manager-specific logic
    return render(request, 'manager_dashboard.html')

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Accountant').exists())
def accountant_dashboard(request):
    # Accountant-specific logic
    return render(request, 'accountant_dashboard.html')



# @login_required(login_url='login')
# def index(request):
#     return render(request, 'dashboard.html')

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

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})

@login_required(login_url='login')
@user_passes_test(lambda u: u.groups.filter(name='Accountant').exists())
def send_for_approval(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    
    if request.method == 'POST':
        # Logic to set transaction for approval (not fully implemented here)
        transaction.approved = False  # Initially set to False
        transaction.manager_approval = None  # Clear manager approval if already set
        transaction.save()
        
        # Redirect to transaction list or wherever appropriate
        return redirect('transaction_list')

    # Handle GET requests if needed

    return redirect('transaction_list')  # Default behavior after POST

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


# def graph(request):
#     transactions = Transaction.objects.all()

#     # Calculate total payments and total receipts
#     total_payments = sum(transaction.payments for transaction in transactions)
#     total_receipts = sum(transaction.receipts for transaction in transactions)

#     context = {
#         'total_payments': total_payments,
#         'total_receipts': total_receipts,
#     }

#     return render(request, 'main.html', context)