import datetime
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class CustomUserManager(UserManager):
    """ユーザーマネージャー"""
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル."""

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    
    DEPARTMENT_CHOICES = [
        ("営業", '営業部'),
        ("経理", '経理部'),
        ("人事", '人事部'),
        ("IT", 'IT部'),
    ]
    department = models.CharField(
        max_length=5,
        choices=DEPARTMENT_CHOICES,
        default="営業部",
    )
        
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in
        between."""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Equipment(models.Model):
    # 備品名称
    name = models.CharField(verbose_name='備品名称', max_length=20, default='')
    # 備品カテゴリー
    EQIPMENT_CHOICES = [
        ("PC", 'PC'),
        ("カメラ", 'カメラ'),
        ("プロジェクター", 'プロジェクター'),
        ("その他", 'その他'),
    ]
    category = models.CharField(
        verbose_name='カテゴリー',
        max_length=5,
        choices=EQIPMENT_CHOICES,
        default="PC",
    )    
    # 購入費用
    price = models.IntegerField(verbose_name='購入費用', default=0)
    # 貸出中
    loaned_out = models.BooleanField(
        default=False,
        help_text=_(
            'if True, being loaned out'),
    )
    # 現在の所持者
    belong_to = models.ForeignKey(User, verbose_name='所持者', on_delete=models.PROTECT, null=True)
    # 返却日
    return_date = models.DateTimeField('return deadline', blank=True, null=True,)
    # 概要
    comment = models.TextField(verbose_name='概要', null=True, blank=True)

    def __str__(self):
        return self.name

    # 返却日の一週間前を知らせる
    def return_day_comming(self):
        return timezone.now() <= self.return_date - datetime.timedelta(days=7)            

