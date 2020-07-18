from django.urls import path
from . import views


urlpatterns = [
    # Course
    path('',views.introduction,name='introduction'),
    path('installation/',views.installation,name='installation'),
    path('first_program/',views.first_program,name='first_program'),
    path('syntax/',views.syntax,name='syntax'),
    path('variable/',views.variable,name='variable'),
    path('data_types/',views.data_types,name='data_types'),
    path('numbers/',views.numbers,name='numbers'),
    path('casting/',views.casting,name='casting'),
    path('strings/',views.strings,name='strings'),
    path('booleans/',views.booleans,name='booleans'),
    path('operators/',views.operators,name='operators'),
    path('lists/',views.lists,name='lists'),
    path('tuples/',views.tuples,name='tuples'),
    path('sets/',views.sets,name='sets'),
    path('dictionaries/',views.dictionaries,name='dictionaries'),
    path('if_else/',views.if_else,name='if_else'),

    # Other Routes
    path('about/',views.about,name='about'),
    
]