from django.shortcuts import redirect, render, get_object_or_404
from .models import UniqueURL, Invite
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .forms import InviteForm
import logging
import json

logger = logging.getLogger(__name__)

# Invitation form view (validates email and creates invite)
def invite_user(request):
    if request.method == "POST":
        form = InviteForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            Invite.objects.create(email=email, is_sent=False)
            return JsonResponse({"message": "Invitation will be sent within a minute!"})
        return JsonResponse({"error": "Invalid email address"}, status=400)
    return render(request, "unique_page.html")

# Generate unique URL and redirect
def base_redirect(request):
    unique_url = UniqueURL.objects.create()
    return redirect('unique_view', unique_id=unique_url.unique_id)

# View for unique URL (checking if expired)
def unique_view(request, unique_id):
    unique_url = get_object_or_404(UniqueURL, unique_id=unique_id)
    base_url = f'{request.scheme}://{request.get_host()}/'
    if unique_url.is_expired:
        return render(request, 'expired.html', {'base_url': base_url})
    return render(request, 'unique_page.html', {'unique_id': unique_id})

# Function to send invite email (API version)
@csrf_exempt
def send_invite(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            recipient_email = data.get('email')

            if not recipient_email:
                return JsonResponse({'error': 'Email is required'}, status=400)

            # Send the invite email
            send_mail(
                'You are invited!',
                'You have been invited to ShareIt. Click the link to join!',
                'trendout.in@gmail.com',
                [recipient_email],
                fail_silently=False,
            )
            return JsonResponse({'message': 'Email sent successfully!'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

# DRF Class-Based View for handling invite (with better logging)
class InviteView(APIView):
    def post(self, request, *args, **kwargs):
        logger.debug(f"Received data: {request.data}")
        email = request.data.get('email')

        if not email:
            return Response({"error": "Email is required"}, status=400)

        try:
            # Process and send the email
            send_mail(
                'You are invited!',
                'You have been invited to ShareIt. Click the link to join!',
                'trendout.in@gmail.com',
                [email],
                fail_silently=False,
            )
            return Response({"message": "Invitation sent!"})
        except Exception as e:
            logger.error(f"Error sending email: {str(e)}")
            return Response({"error": str(e)}, status=500)

# Function-Based View for Invite (if you prefer not using class-based views)
@api_view(['POST'])
def invite_view(request):
    logger.debug(f"Request Data: {request.data}")
    email = request.data.get('email')

    if not email:
        return Response({"error": "Email is required"}, status=400)

    try:
        send_mail(
            'You are invited!',
            'You have been invited to ShareIt. Click the link to join!',
            'trendout.in@gmail.com',
            [email],
            fail_silently=False,
        )
        return Response({"message": "Invitation sent!"})
    except Exception as e:
        logger.error(f"Error sending email: {str(e)}")
        return Response({"error": str(e)}, status=500)





from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def invite_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            content = data.get('content')  # Get content from the request

            if not email:
                return JsonResponse({"error": "Email is required"}, status=400)

            if not content:
                return JsonResponse({"error": "Content is required"}, status=400)

            # Generate a unique URL for the invite (you can change this to use actual URL generation logic)
            invite_url = f"{request.scheme}://{request.get_host()}/unique/{email}/"

            # Create the email message including content and invite link
            message = f"""
                You have been invited to ShareIt!

                Here is the content from the inviter:
                {content}

                To join, click the link below:
                {invite_url}
            """

            # Send the email
            send_mail(
                'You are invited to ShareIt!',
                message,
                'trendout.in@gmail.com',  # From email address
                [email],  # Recipient email address
                fail_silently=False,
            )

            return JsonResponse({"message": "Invitation sent successfully!"})
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)



from django.core.mail import EmailMultiAlternatives

def send_html_email():
    subject = "Welcome to Our Service"
    from_email = "trendout.in@gmail.com"  # Replace with your email
    to_email = "suri14srr@gmail.com"  # Replace with the recipient's email

    # Plain text version (fallback)
    text_content = "This is the plain text version of the email. Visit our site for more details."

    # HTML content
    html_content = """
    <html>
        <body>
            <h1>Welcome to Our Service!</h1>
            <p>We're glad to have you here. Check out our <a href="https://example.com">website</a>.</p>
            <p>Best regards,<br>Your Team</p>
        </body>
    </html>
    """

    # Create the email
    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_content, "text/html")

    # Send the email
    email.send()

    print("HTML email sent successfully!")
