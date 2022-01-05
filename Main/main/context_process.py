from typing import ContextManager
from main.models import Post


def searchFunction(request):
    search_context={}
    posts= Post.objects.all()
    if "search" in request.GET:
        query = request.GET.get("q")
        
        # filter start
        search_box = request.GET.get("search-box")
        print("\n\n\n"+search_box)
        if search_box == "description":
            objects = posts.filter(content__icontains=query)
        else:
            objects = posts.filter(title__icontains=query)
        # filter end
        
      
        search_context = {
            "objects":objects,
            "query":query,
        }
    return search_context