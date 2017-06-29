from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

# from django.http import HttpResponse
# from django.template import loader
# from django.shortcuts import render, get_object_or_404
# from .models import Album, Song
# from django.http import Http404

#  def index(request):
#     html = ''
#     all_albums = Album.objects.all()
#     template = loader.get_template('music/index.html')
#     context = {
#        "all_albums": all_albums,
#
#     }
#     return HttpResponse(template.render(context,request))
#
#     #
#     # for album in all_albums:
#     #     url = '/music/'+str(album.id)+'/'
#     #     html += '<a href="'+url+'">' + album.album_title + '</a><br>'
#
#
#     # return HttpResponse(html)
#
# def detail(request,album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     #return HttpResponse("<h2>Details for album ID "+str(album_id)+" </h2>")
#     # try:
#     #     album = Album.objects.get(pk = album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("ALBUM does not exist")
#     return render(request,"music/detail.html",{"album": album})
#
# def favorite(request,album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         return render(request,'music/detail.html', {
#             "album": album,
#             "error_message": "NO SONG VALID",
#         })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, "music/detail.html", {"album": album})
#
#
#
