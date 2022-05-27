from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, timedelta

class Tag(models.Model):
    name = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name

class AccountQuerySet(models.QuerySet):
    def personal(self):
        return self.filter(account_type=Account.AccountType.PERSONAL)

    def foreign(self):
        return self.filter(account_type=Account.AccountType.FOREIGN)

    def active(self):
        return self.filter(active=True)

    def inactive(self):
        return self.filter(active=False)

    def shown_on_dashboard(self):
        return self.filter(show_on_dashboard=True)

class Account(models.Model):
    class AccountType(models.IntegerChoices):
        PERSONAL = 1, ('Personal')
        FOREIGN = 2, ('Foreign')
        SYSTEM = 3, ('System')

    name = models.CharField(max_length=64)
    account_type = models.IntegerField(choices=AccountType.choices, default=AccountType.PERSONAL)
    active = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now=True)
    show_on_dashboard = models.BooleanField(default=False)
    iban = models.CharField(max_length=34, blank=True, null=True)
    import_ibans = models.TextField(default='[]')
    import_names = models.TextField(default='[]')

    objects = AccountQuerySet.as_manager()

    class Meta:
        ordering = ['-active', 'name']
        unique_together = (('name', 'account_type'),)

    def __str__(self):
        return self.name

    @property
    def account_type_str(self):
        return Account.AccountType.labels[self.account_type - 1]

    @property
    def is_personal(self):
        return self.account_type == Account.AccountType.PERSONAL

    @property
    def transaction_num(self):
        """
        TODO do we really want the number of splits?
        """
        return Split.objects.filter(account=self).count()

    @property
    def balance(self):
        return self.balance_on(date.today())

    def balance_on(self, date):
        return Split.objects.filter(account=self, date__lte=date).aggregate(
            models.Sum('amount'))['amount__sum'] or 0

    def get_absolute_url(self):
        return reverse('account_view', args=[self.pk])

    def get_data_points(self, dstart=date.today() - timedelta(days=365),
                        dend=date.today(), steps=30):
        step = (dend - dstart) / steps
        if step < timedelta(days=1):
            step = timedelta(days=1)
            steps = int((dend - dstart) / step)
        data_points = []
        balance = self.balance_on(dstart - timedelta(days=1))
        transactions = list(Split.objects.prefetch_related('transaction').filter(
            account_id=self.pk).date_range(dstart, dend).order_by(
            '-transaction__date'))
        for i in range(steps):
            while len(transactions) > 0 and transactions[-1].transaction.date <= dstart:
                t = transactions.pop()
                balance += t.amount
            data_points.append((dstart, balance))
            dstart += step
        for t in transactions:
            balance += t.amount
        data_points.append((dend, balance))
        return data_points

    def set_initial_balance(self, amount):
        system = Account.objects.get(account_type=Account.AccountType.SYSTEM)
        transaction = Transaction.objects.create(title=_('Initial Balance'),
                                                 transaction_type=Transaction.SYSTEM,
                                                 src=system,
                                                 dst=self,
                                                 amount=amount)
        Split.objects.create(transaction=transaction, amount=-amount,
                             account=system, opposing_account=self)
        Split.objects.create(transaction=transaction, amount=amount,
                             account=self, opposing_account=system)



class Stiver(models.Model):
    item = models.CharField(max_length=20, verbose_name='名称', null=True)
    money = models.FloatField(verbose_name='金额', null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    note = models.TextField(max_length=1000, null=True, verbose_name='记录')
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('stiver-detail', kwargs = {'pk': self.pk})
