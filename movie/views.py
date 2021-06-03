from django.shortcuts import render,redirect
from movie import models
# Create your views here.
def home(request):

    return render(request,'movie/home.html')

def movie_list(request):
    return render(request,'movie/list.html')

def news(request):
    return render(request,'movie/news.html')

def detail(request):
    mno=request.GET['mno']
    #mno,title,poster,regdate,genre,grade,story,key
    detail_data=models.movie_detail(int(mno))
    recv={"mno":detail_data[0],"title":detail_data[1],"poster":detail_data[2],"regdate":detail_data[3],
           "genre":detail_data[4],"grade":detail_data[5],"story":detail_data[6],"key":detail_data[7]}
    return render(request,'movie/detail.html',recv)

def recommand(request):
    return render(request,'movie/recomm.html')


