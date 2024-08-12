# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, UserProfileForm, FAQForm
from .models import UserProfile, FAQ  # Ensure FAQ is imported
from .forms import FAQSearchForm  # Add this import
from .services.commands import FAQCommandService
from .services.queries import FAQQueryService
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def faq_list(request):
    faqs = FAQ.objects.filter(is_approved=True)
    form = FAQForm()
    search_form = FAQSearchForm(request.GET or None)

    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            if request.user.is_authenticated:
                faq.submitted_by = request.user
            faq.save()

            # Send an email to the user
            send_mail(
                'Question Received - Concordia University',
                f'Thank you for your question. We have received your question: "{faq.question}" and will respond to it soon.',
                settings.EMAIL_HOST_USER,
                [request.user.email],
                fail_silently=False,
            )

            return redirect('faq_list')

    if search_form.is_valid():
        search_query = search_form.cleaned_data['search_query']
        faqs = faqs.filter(question__icontains=search_query)

    context = {
        'faqs': faqs,
        'form': form,
        'search_form': search_form,
    }
    return render(request, 'faq_list.html', context)



@login_required
def profile(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = CustomUserCreationForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def submit_faq(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            FAQCommandService.create_faq(
                question=form.cleaned_data['question'],
                answer=form.cleaned_data['answer'],
                submitted_by=request.user
            )
            return redirect('faq_list')
    else:
        form = FAQForm()
    return render(request, 'submit_faq.html', {'form': form})

@login_required
def approve_faq(request, faq_id):
    if not request.user.is_superuser:
        return redirect('home')
    faq = FAQ.objects.get(id=faq_id)
    faq.is_approved = True
    faq.save()
    return redirect('faq_list')

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FAQForm

@login_required
def submit_faq(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.submitted_by = request.user
            faq.save()
            return redirect('faq_list')
    else:
        form = FAQForm()
    return render(request, 'submit_faq.html', {'form': form})

# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm

def event_list(request):
    events = Event.objects.all().order_by('date', 'time')
    return render(request, 'event_list.html', {'events': events})

def event_list(request):
    events = Event.objects.all().order_by('date', 'time')
    return render(request, 'event_list.html', {'events': events})

def faq_detail(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    return render(request, 'faq_detail.html', {'faq': faq})