from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Users
from .forms import RegisterUserForm, ArticleForm, LoginForm

# Create your views here.

# TODO Set up language with cookies from users https://docs.djangoproject.com/en/4.0/topics/i18n/translation/#explicitly-setting-the-active-language

# @unauthenticated_user
def registerPage (request):
    form = RegisterUserForm()
    if request.method == 'POST' :
        form = RegisterUserForm(request.POST)
        if form.is_valid ():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            #Added username after video because of error returning custo
            Customer.objects.create(
                user=user,
                name=user.username,
                )
            # messages.success (request, Account was created for + username)

            return redirect('login')


    context = {'form' : form}
    return render(request, 'accounts/register.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me', False)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
            if remember_me == False:
                # <-- Here if the remember me is False, 
                # that is why expiry is set to 0 seconds. 
                # So it will automatically close the session
                # after the browser is closed.
                request.session.set_expiry(0)  

            # else browser session will be as long as 
            # the session cookie time "SESSION_COOKIE_AGE"
        else:
            messages.success(request, "Error logging in")
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('home')


def home_section(request):
    return render(request, 'home.html', {})

def trending_screen(request, *args, **kargs):
    # Display the 10 articles with the most visits in the last 72 hours (cookies ) 
    article_list = Article.objects.all()
    # displayArticlesNum = 12 # request.article_show
    context = {}

    return render(request, "trending.html", {'article_list': article_list})

def articles_display(request, *args, **kwargs):
    return render(request, "articles_display", {})

def read_article(request, art_id, *args, **kwargs):
    obj = Article.objects.get(pk=art_id)
    return render(request, "user_article.html", {obj})

def author_page(request, author_id, *args, **kwargs):
    author = request.user
    author_articles = Article.objects.all().filter(author_id=author.id)
    return render(request, "author_page.html", {author_articles})

# def login(request, ):
# 	return render(request, "", {})

# TODO Set up use of forms, crsf tokens



# def make_article(request):

# 	f = ArticleForm(request.POST)
# 	if f.is_valid():
# 		new_article = f.save()

# 	return render(request, "make_article.html", {"form": f})



def post_article(name, message):
    # Code for actually sending the message goes here

	class PostData(forms.Form):
		name = forms.CharField()
		message = forms.CharField(widget=forms.Textarea)

def profile(request, *args, **kwargs):
    return render(request, 'profile.html', {})

def graphsAndData(request, *args, **kwargs):
    return render(request, 'data.html', {})

def inbox(request, *args, **kwargs):
    return render(request, 'inbox.html', {})

def settings_page(request, *args, **kwargs):
    user = request.user
    form = RegisterForm(instance=user)
    context = {'form':forms}
    return render(request, 'settings.html', context)

def user_files(request, *args, **kwargs):
    return render(request, 'user_files.html', {})

def favourites(request, *args, **kwargs):
    return render(request, 'liked_articles.html', {})

def user_file_manager(request, *args, **kwargs):
    return render(request, 'user_files.html', {})


def make_article(request):
    # The request method 'POST' indicates
    # that the form was submitted

    user_id = request.user.id
    author = Users.objects.filter(id=user_id).first()
    if request.user.is_authenticated:
        if request.method == 'POST':  # 1
            # Create a form instance with the submitted data
            form = ArticleForm(request.POST, {'author': author})  # 2
            # Validate the form
            if form.is_valid():  # 3
                # If the form is valid, perform some kind of
                # operation, for example sending a message
                article = form.save()
                # After the operation was successful,
                # redirect to some other page
                return redirect(reverse(read_article, args = article.id))  # 4
        else:  # 5
            # Create an empty form instance
            form = ArticleForm()
    else:
        pass
    request.session


    context = {
        'form': form,
        'id': user_id
    }

    return render(request, 'make_article.html', context)

# TODO Make more views for different sections of the app

import datetime

#TODO Add a cookie to count the number of visitors with 3 days expiration date
#TODO All time counter of article visits

def set_cookie(response, key, value, days_expire=3):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    cookie = response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
        domain=settings.SESSION_COOKIE_DOMAIN,
        secure=settings.SESSION_COOKIE_SECURE or None,
    )
    