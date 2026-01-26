from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from .models import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ML'))
from summary_utils import generate_summary
from django.contrib import messages

def first(request):
    return render(request,'index.html')
def index(request):
    return render(request,'index.html')
def addreg(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('phone_number')
        c=request.POST.get('email')
        d=request.POST.get('password')
        r=request.POST.get('role')
        if r == 'user':
            e=regtable(name=a,phone_number=b,email=c,password=d,role=r)
            e.save()
        elif r == 'reporter':
            exp = request.POST.get('experience_years', 0)
            spec = request.POST.get('specialization', '')
            bio = request.POST.get('bio', '')
            Reporter.objects.create(name=a, phone_number=b, email=c, password=d, experience_years=exp, specialization=spec, bio=bio)
    return redirect(login) 

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def addlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['admin'] = 'admin'
        return render(request,'index.html')

    elif regtable.objects.filter(email=email,password=password).exists():
            print("user login")
            userdetails=regtable.objects.get(email=request.POST['email'], password=password)
            request.session['uid'] = userdetails.id
            return render(request,'index.html')

    elif Reporter.objects.filter(email=email,password=password).exists():
            reporterdetails=Reporter.objects.get(email=request.POST['email'], password=password)
            request.session['rid'] = reporterdetails.id
            return render(request,'index.html')

    else:
        return render(request, 'login.html', {'message':'Invalid Email or Password'})
    



def v_users(request):
    user=regtable.objects.all()
    return render(request,'viewusers.html',{'result':user})




def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)

def add_news_article(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        tags = request.POST.get('tags')
        author_id = request.session.get('rid')
        if author_id:
            author = Reporter.objects.get(id=author_id)
            # Generate summary
            summary = generate_summary(content)
            NewsArticle.objects.create(title=title, content=content, summary=summary, author=author, category=category, tags=tags)
            return redirect(index)
    return render(request, 'add_news_article.html')

def view_news(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    
    articles = NewsArticle.objects.all().order_by('-published_date')
    
    # Apply filters
    if query:
        articles = articles.filter(title__icontains=query)
    if category:
        articles = articles.filter(category=category)
    
    # Process tags for each article
    for article in articles:
        if article.tags:
            article.tag_list = [tag.strip() for tag in article.tags.split(',') if tag.strip()]
        else:
            article.tag_list = []
    
    return render(request, 'view_news.html', {
        'articles': articles, 
        'query': query,
        'selected_category': category
    })

def manage_articles(request):
    if not request.session.get('admin'):
        return redirect('login')
    
    articles = NewsArticle.objects.all().order_by('-published_date')
    
    # Handle delete action
    if request.method == 'POST' and 'delete_article' in request.POST:
        article_id = request.POST.get('article_id')
        try:
            article = NewsArticle.objects.get(id=article_id)
            article.delete()
            messages.success(request, 'Article deleted successfully.')
        except NewsArticle.DoesNotExist:
            messages.error(request, 'Article not found.')
        return redirect('manage_articles')
    
    return render(request, 'manage_articles.html', {'articles': articles})