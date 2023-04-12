from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Listing, Bid, Category, Comment, Soled, Watchlist
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

def avalib_list(request, id):
    listing = Listing.objects.get(id=id)
    
    price = listing.price

    
    if request.method == 'POST':

        bid = int(request.POST.get("bid"))
        if not bid or bid <= int(price):
            message = messages.error(request, "Please input correct value ")
            return redirect("index")
        s = Bid.objects.create (amount=bid, bidder=request.user, listing=listing)
        s.save()
        messages.success(request, "Your bid has been placed successfully.")
        #Listing.objects.filter(id=id).update(price=bid)
        return redirect("avalib_list", id=id)

    return render(request, 'auctions/avalib_list.html', {
        'listing': listing,
        "bids":Bid.objects.all()
        })



def index(request):
    listings = Listing.objects.all()
    bids = Bid.objects.all()
    if request.method == "POST":
        listing = Listing.objects.filter(id=id)
        watchlist = Watchlist.objects.create(listing = listing, user=request.user )
        watchlist.save()
        return redirect(request, "auctions/watchlist.html", id=id)
    return render(request, "auctions/index.html", {
        "listings": listings,
        "bids": bids
    })

@login_required
def my_listings(request):
    user = request.user
    listings = Listing.objects.filter(user=user)

        
    return render(request, "auctions/my_listings.html", {
        "listings":listings,
        "bids": Bid.objects.all()
    })
@login_required
def sell_listing(request, id):
    listing = Listing.objects.get(id=id)
    try:
        amount = Bid.objects.get(listing=listing)
        value = amount.amount
    except ObjectDoesNotExist :
        value = False
    if request.method == 'POST':
        if value:
            listing.inactive = True
            listing.save()
            sold = Soled.objects.create(buyer=request.user, seller=listing.user,  listing=listing, soled_price=Bid.objects.get(listing=listing))
            sold.save()
            messages.success(request, "Listing has been sold.")
        else:
            messages.error(request, "There is no bid  ")
        return redirect('my_listings')
    return render(request, 'auctions/sell_listing.html', {'listing': listing})

@login_required
def del_listing(request, id):
    listing=Listing.objects.get(id=id)

    if request.method == 'POST':
        #listing.inactive = True
        listing.delete()
        messages.success(request, "Listing has been deleted")
        return redirect('my_listings')
    return render(request, 'auctions/del_listing.html', {'listing':listing})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


@login_required
def history (request):

    return render(request, "auctions/history.html", {"listings":Soled.objects.all()})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def listing(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        price = request.POST.get("price")
        img = request.POST.get("img")
        # Проверяем наличие всех полей формы
        if not title or not description or not price:
            message = messages.error(request, "Please fill all the fields")
            return redirect("listing")

        # Создаем объект Listing и сохраняем его в базу данных
        listing = Listing.objects.create(title=title, description=description, price=price, img=img, user=request.user)
        listing.save()
        return redirect("index")

    return render(request, "auctions/listing.html")


"""def avalib_list(request):
    listings = Listing.objects.all()

    return render(request, "auctions/avalib_list.html",{
        "listings" : listings
    })"""


@login_required
def watchlist (request):
    return render(request, "auctions/watchlist.html", {
        "listings": Listing.objects.all(),
        "bids": Bid.objects.all()
    })














"""@login_required
def listing (request):
    if request.method == "POST":
        title = request.POST.get("title")
        decription = request.POST.get("decription")
        price = request.POST.get("price")
        if title or decription or price is None:
            return render(request, "auctions/lising.html" ,{
                "message":"Fill all fields"
            })
        lisitng = Listing.objects.create(title=title, decription=decription, price=price, user=request.user)
        listing.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/listing.html")"""

    


"""Users should be able to visit a page to create a new listing. 
They should be able to specify a title for the listing, a text-based description, and what the starting bid
 should be. Users should also optionally be able to provide a URL
  for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.)."""