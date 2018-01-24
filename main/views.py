from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SearchForm
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import json

# Create your views here.


class StdOutListener(StreamListener):

    def on_data(self, data):
        try:
            client = MongoClient('mongodb://localhost:27017')
            db = client.temp
            collection = db.data
            result = collection.insert_one(json.loads(data))
            print('One post: {0}'.format(result.inserted_id))
        except Exception as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)


def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/search/')
    else:
        form = SearchForm()
    return render(request, 'index.html', {'form': form})


def search(request):
    if request.method == 'POST':
        searchParameter = request.POST['search']  # received

        auth = OAuthHandler('4Zb7o0O8OO2X9D8ZwZbMim0VC',
                            'AuhG7FRlmcnIsangasWB20bJk41cYFgHOQQ61tK8PkujlR7gKI')
        auth.set_access_token('1100686363-6JxQIno5T8UMPQeWyaH783qrxxJJrmwbLJCEtoF',
                              'GqgnME3MRfOQL79TzWuH5S9fJOgXXogdAwyVDzGSk4ovD')

        l = StdOutListener()
        stream = Stream(auth, l)
        stream.filter(track=[searchParameter])

    return render(request, 'data.html', {'data': form})


def filter(request):
    if request.method == 'POST':
        print(request.POST['filterField'])
        print(request.POST['filterValue'])
    client = MongoClient('mongodb://localhost:27017')
    db = client.temp
    collection = db.data
    result = list(collection.find({}))[-1]

    return render(request, 'data.html', {'data': result, 'options': result.keys()})


def results(request):
    client = MongoClient('mongodb://localhost:27017')
    db = client.temp
    collection = db.data
    if request.method == 'POST':
        filter = request.POST['filter']  # received
        filterValue = request.POST['filterValue']  # received
        result = list(collection.find({}))[-1]
    else:
        result = list(collection.find({}))[-1]

    return render(request, 'data.html', {'data': result, 'options': result.keys()})
