from django.shortcuts import render
from django.views import generic
from .models import Song, SongPart, SongPartAction
from django.db.models import Min
# Create your views here.

class IndexView(generic.ListView):
    template_name = "songs/index.html"
    context_object_name = "song_list"
    def get_queryset(self):
        return Song.objects.order_by("-title")[:5]

class DetailView(generic.DetailView):
    model = Song
    template_name = "songs/detail.html"
    context_object_name = 'song'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        song = context['song']
        song_parts = SongPart.objects.filter(song_id=song).order_by('part_order')
        
        # Przygotuj słownik, który przyporządkuje kod z choices do pełnej nazwy opisowej
        action_object_choices = dict(SongPartAction._meta.get_field('action_object').choices)
        parts = [] 
        for song_part in song_parts:
            
            object_actions = []
            action_objects_query = SongPartAction.objects.filter(song_part=song_part).values('action_object').annotate(min_action_order=Min('action_order')).order_by('min_action_order')
            for action_object in action_objects_query:
                action_object_code = action_object['action_object']
                actions_for_object = SongPartAction.objects.filter(song_part=song_part, action_object = action_object_code).order_by('action_order') 
                
                actions_descriptions = [action.action_description for action in actions_for_object]
                action_object_name = action_object_choices[action_object_code]

                object_actions.append( { 'object_name': action_object_name,
                                         'actions_descriptions': actions_descriptions })    
           
            parts.append( { 'part_id' : song_part.id,
                            'part_name' : song_part.part_name,
                            'objects_actions': object_actions} )
    
            
        context['song_parts'] = parts
        #context['song_parts'] = song_parts
        return context


