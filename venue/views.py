from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Hangout
from blog.models import Post
import requests

class VenueListView(ListView):
    # url = "https://hotels4.p.rapidapi.com/locations/v2/search"
    # querystring1 = {"query":"chicago","locale":"en_US","currency":"USD"}
    # querystring2 = {"query":"new york","locale":"en_US","currency":"USD"}
    # querystring3 = {"query":"los angeles","locale":"en_US","currency":"USD"}
    # querystring4 = {"query":"boston","locale":"en_US","currency":"USD"}
    # querystring5 = {"query":"san jose","locale":"en_US","currency":"USD"}
    # headers = {
    #     "X-RapidAPI-Key": "4c24c7d3b7msha9c2def7540d066p12db18jsnc7c423d08cee",
    #     "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    # }
    # response1 = requests.request("GET", url, headers=headers, params=querystring1).json()
    # for i in response1['suggestions'][1]['entities']:
    #     obj = Hangout(title = i['name'], location = 'Chicago')
    #     obj.save()
    # response2 = requests.request("GET", url, headers=headers, params=querystring2).json()
    # for i in response2['suggestions'][1]['entities']:
    #     obj = Hangout(title = i['name'], location = 'New York')
    #     obj.save()
    # response3 = requests.request("GET", url, headers=headers, params=querystring3).json()
    # for i in response3['suggestions'][1]['entities']:
    #     obj = Hangout(title = i['name'], location = 'Los Angeles')
    #     obj.save()
    # response4 = requests.request("GET", url, headers=headers, params=querystring4).json()
    # for i in response4['suggestions'][1]['entities']:
    #     obj = Hangout(title = i['name'], location = 'Boston')
    #     obj.save()
    # response5 = requests.request("GET", url, headers=headers, params=querystring5).json()
    # for i in response5['suggestions'][1]['entities']:
    #     obj = Hangout(title = i['name'], location = 'San Jose')
    #     obj.save()
    # url1 = "https://restaurants-near-me-usa.p.rapidapi.com/restaurants/location/state/MI/city/Detroit/0"
    # url2 = "https://restaurants-near-me-usa.p.rapidapi.com/restaurants/location/state/MI/city/West%20bloomfield/0"
    # url3 = "https://restaurants-near-me-usa.p.rapidapi.com/restaurants/location/state/MI/city/Frankenmuth/0"
    # headers = {
    #     "X-RapidAPI-Key": "4c24c7d3b7msha9c2def7540d066p12db18jsnc7c423d08cee",
    #     "X-RapidAPI-Host": "restaurants-near-me-usa.p.rapidapi.com"
    # }
    # response1 = requests.request("GET", url1, headers=headers).json()
    # for i in response1['restaurants']:
    #     obj = Hangout(title = i['restaurantName'], location = i['cityName'], type = 'restaurant')
    #     obj.save()
    # response2 = requests.request("GET", url2, headers=headers).json()
    # for i in response2['restaurants']:
    #     obj = Hangout(title = i['restaurantName'], location = i['cityName'], type = 'restaurant')
    #     obj.save()
    # response3 = requests.request("GET", url3, headers=headers).json()
    # for i in response3['restaurants']:
    #     obj = Hangout(title = i['restaurantName'], location = i['cityName'], type = 'restaurant')
    #     obj.save()
    # url = "https://argentina-movie-theatres.p.rapidapi.com/cinemas"
    # headers = {
    #     "X-RapidAPI-Key": "4c24c7d3b7msha9c2def7540d066p12db18jsnc7c423d08cee",
    #     "X-RapidAPI-Host": "argentina-movie-theatres.p.rapidapi.com"
    # }
    # response = requests.request("GET", url, headers=headers).json()
    # for i in range(6, 11):
    #     obj = Hangout(title = response[i]['name'], location = 'Buenos Aires', type = 'theatre')
    #     obj.save()
    model = Hangout
    template_name = 'venue/venue_home.html'
    context_object_name = 'venues'
    ordering = ['-rating']
    paginate_by = 8

class VenuePostListView(ListView):
    model = Hangout
    template_name = 'venue/venue_posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        obj = get_object_or_404(Hangout, id=self.kwargs.get('id'))
        return Post.objects.filter(venue=obj).order_by('-rating')