from django.forms import *
from django.forms.widgets import *
from django.forms.extras.widgets import *
import datetime

# Contact Form
from captcha.fields import CaptchaField
from tamulug.settings import CONTACT_FORM_EMAIL
from tamulug.mailer import mail_send
class ContactSubmission():
  def __init__(self, subject, message, name, phone, email):
    self.subject = subject
    self.message = message
    self.name = name
    self.email = email

class ContactForm(Form):
  subject = CharField(max_length=100)
  message = CharField(max_length=2000, widget=Textarea(attrs={'cols':35, 'rows': 5}))
  name = CharField(max_length=200)
  email = EmailField()
  cc_myself = BooleanField(required=False)
  captcha = CaptchaField()

  def save(self):
    fd = self.cleaned_data
    cs = ContactSubmission(fd['subject'], fd['message'], fd['name'], fd['email'])
    mail_send([CONTACT_FORM_EMAIL], {'submission': cs}, 'mail/contact_form')
    if fd['cc_myself'] and fd['email']:
      mail_send([fd['email']], cs, 'mail/contact_form')
    return cs
