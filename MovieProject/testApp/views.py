from django.shortcuts import render
from testApp.models import MovieInfo
from testApp.forms import MovieInfoDisplay

# Create your views here.
def index_view(request):
    return render(request,"testApp/index.html")

def addmovie_view(request):
    form=MovieInfoDisplay()
    if request.method=="POST":
        form=MovieInfoDisplay(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)
    return render(request,"testApp/addmovie.html",{'form':form})


def movielist_view(request):
    movie_list=MovieInfo.objects.order_by('releasedate')
    my_dict={'movie_list':movie_list}
    return render(request,"testApp/movielist.html",context=my_dict)
