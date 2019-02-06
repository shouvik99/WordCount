from django.shortcuts import render
from django.http import HttpResponse
import operator

# Create your views here.

def index(request):
    return render(request,'index.html')

def counted(request):
    data = request.GET['texts']
    words = data.split()
    length = len(words)

    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word]=1

    sorted_list = sorted(word_dict.items() ,key=operator.itemgetter(1), reverse = True)

    return render(request,'counted.html',{ 'countable_text':data ,'total_words':length ,'word_dict':sorted_list })

def about(request):
    return render(request,'about.html')
