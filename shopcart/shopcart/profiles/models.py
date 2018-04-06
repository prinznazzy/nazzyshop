from __future__ import unicode_literals
from django.db import models

# from django.core.urlresolvers import reverse


# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name

# class LoginAfterPasswordChangeView(PasswordChangeView):
#     @property
#     def success_url(self):
#         return reverse_lazy('generic:password_change_success')

# login_after_password_change = login_required(LoginAfterPasswordChangeView.as_view())

    # def get_absolute_url(self):
	# 	return reverse('home', args=[self.slug])
