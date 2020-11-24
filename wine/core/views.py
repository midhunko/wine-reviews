from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Wine, UserProfile, Review
import datetime


# home page
def index(request):
    wine = Wine.objects.all()
    return render(request, 'index.html', {'wine': wine})


# login method
def log_in(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        usercheck = authenticate(request, username=name, password=password)

        if usercheck:
            login(request, usercheck)
            return HttpResponseRedirect(reverse(index))
        else:
            error = 'User not found!'
            return render(request, 'log_in.html', {'error': error})
    else:
        return render(request, 'log_in.html')


# logout method
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))


# signup method
def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        userfound = UserProfile.objects.filter(name=name).exists()  # check if the user exists, if not creates it

        if not userfound:
            new_user = User.objects.create_user(
                username=name,
                password=password
            )
            user = UserProfile.objects.create(
                user=new_user,
                name=name,
                password=password
            )
            return render(request, 'log_in.html')
        else:
            error = 'User already exists!'
            return render(request, 'sign_up.html', {'error': error})
    else:
        return render(request, 'sign_up.html')


# method for list all reviews
def review_list(request):
    rlist = Review.objects.order_by('-pub_date')
    return render(request, 'review_list.html', {'rlist': rlist})


'''def review_detail(request, r_id):
    review = get_object_or_404(Review, id=r_id)
    return render(request, 'review_detail.html')'''


# to add new reviews
def add_review(request, w_id):
    wines = get_object_or_404(Wine, pk=w_id)
    users = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        review = request.POST.get('review')
        pubdate = datetime.datetime.now()
        user_exist = Review.objects.filter(user=users)  # filters first by user and then user with the wine name
        review_exist = user_exist.filter(wine=wines).exists()

        if not review_exist:
            new_review = Review.objects.create(
                user=users,
                wine=wines,
                review=review,
                pub_date=pubdate
            )
            return HttpResponseRedirect(reverse(review_list))
        else:
            return HttpResponse('Review already exists!')
    else:
        return render(request, 'add_review.html', {'wines': wines})
