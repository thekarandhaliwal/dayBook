# myapp/management/commands/create_users.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Create users and assign them to groups'

    def handle(self, *args, **kwargs):
        # Create users
        accountant = User.objects.create_user('accountant', 'accountant@example.com', 'password')
        manager = User.objects.create_user('manager', 'manager@example.com', 'password')
        admin = User.objects.create_user('admin', 'admin@example.com', 'password')

        # Assign users to groups
        accountant_group = Group.objects.get(name='Accountant')
        manager_group = Group.objects.get(name='Manager')
        admin_group = Group.objects.get(name='Admin')

        accountant.groups.add(accountant_group)
        manager.groups.add(manager_group)
        admin.groups.add(admin_group)

        self.stdout.write(self.style.SUCCESS('Successfully created users and assigned them to groups'))
