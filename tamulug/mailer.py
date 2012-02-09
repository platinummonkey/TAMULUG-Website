from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from vobject import iCalendar
from email.mime.text import MIMEText
import datetime

def mail_send(recipients, contextDict, templateBase):
  # contextDict is {'foo': var}
  from_email = 'no-reply@tamulug.tamu.edu'
  subject_t = get_template(templateBase+'_subject.txt')
  plaintext_t = get_template(templateBase+'.txt')
  html_t = get_template(templateBase+'.html')
  d = Context(contextDict)
  subject_content = subject_t.render(d).rstrip() # need to strip off newline (SMTP error otherwise)
  plaintext_content = plaintext_t.render(d)
  html_content = html_t.render(d)
  msg = EmailMultiAlternatives(subject_content, plaintext_content, from_email, recipients)
  msg.attach_alternative(html_content, "text/html")
  msg.send()
