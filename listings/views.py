from django.shortcuts import render

from .models import Listing

def index(request):
    listings = Listing.objects.all()        #fetch all listings, no raw sql queries

    context = {
        'listings': listings         #passing data into dicitonary
    }

    return render(request, 'listings/listings.html', context) #passing dictionary into template

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')


