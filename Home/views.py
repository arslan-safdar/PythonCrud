from django.shortcuts import render
from django.http import HttpResponse

persons = [
    {'name':"Arslan" , 'age' : 28},
     {'name':"Idrees" , 'age' : 28},
      {'name':"safdar" , 'age' : 28},
       {'name':"Nabeel" , 'age' : 28},
        {'name':"Adeel" , 'age' : 28}
]
text = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias perferendis a sed quis reprehenderit cumque, accusantium, atque commodi nam fugiat consequatur harum nobis doloremque necessitatibus officia, doloribus ratione quos officiis.
"""
def Testing(response):
    return render(response , 'home/index.html',context={'persons' : persons,'text':text})