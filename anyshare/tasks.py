from celery import shared_task
from django.core.mail import send_mail
from .models import Invite

@shared_task
def send_invitation_emails():
    invites = Invite.objects.filter(is_sent=False)
    for invite in invites:
        try:
            # Send email
            send_mail(
                subject="You're Invited!",
                message="You've been invited to join ShareIt!",
                from_email="trendout.in@gmail.com",
                recipient_list=[invite.email],
            )
            # Mark as sent
            invite.is_sent = True
            invite.save()
        except Exception as e:
            print(f"Failed to send email to {invite.email}: {e}")
