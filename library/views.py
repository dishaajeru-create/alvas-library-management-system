from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Member, Book, Issue
import random
def home(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    books = Book.objects.all()
    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query)
    if category:
        books = books.filter(category__iexact=category)
    categories = Book.objects.values_list('category', flat=True).distinct()
    return render(request, 'library/home.html', {
        'books': books,
        'categories': categories,
        'query': query,
        'selected_category': category,
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'library/register.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            member_id = f"MEM{random.randint(1000, 9999)}"
            Member.objects.create(user=user, member_id=member_id)
            messages.success(request, f'Account created! Your Member ID is {member_id}. Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'library/register.html', {'form': form})
def issue_book(request):
    books = Book.objects.filter(available_copies__gt=0)
    members = Member.objects.filter(is_active_member=True)
    if request.method == 'POST':
        book = Book.objects.get(id=request.POST['book_id'])
        member = Member.objects.get(id=request.POST['member_id'])
        Issue.objects.create(book=book, member=member)
        book.available_copies -= 1
        book.save()
        messages.success(request, f'"{book.title}" issued to {member.member_id}')
        return redirect('issue_book')
    return render(request, 'library/issue_book.html', {'books': books, 'members': members})
def return_book(request):
    active_issues = Issue.objects.filter(is_returned=False)
    if request.method == 'POST':
        issue = Issue.objects.get(id=request.POST['issue_id'])
        issue.return_date = timezone.now()
        issue.is_returned = True
        issue.fine_amount = issue.calculate_fine()
        issue.save()
        issue.book.available_copies += 1
        issue.book.save()
        messages.success(request, f'"{issue.book.title}" returned. Fine: ₹{issue.fine_amount}')
        return redirect('return_book')
    return render(request, 'library/return_book.html', {'active_issues': active_issues})