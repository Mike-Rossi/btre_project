from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)        #fetch all listings, no raw sql queries

    paginator = Paginator(listings, 3) 
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings         #passing data into dicitonary
    }

    return render(request, 'listings/listings.html', context) #passing dictionary into template

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')


