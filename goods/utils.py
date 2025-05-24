from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q
from goods.models import Products


def q_search(queary):

    if queary.isdigit() and len(queary) <= 5:
        return Products.objects.filter(id=int(queary))
    
    vector = SearchVector("name", "description")
    query = SearchQuery(queary) 

    return Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")


#    keyword = [word for word in queary.split() if len(word) > 2]

#    q_objects = Q()

#        q_objects |= Q(description__icontains=token)
#       q_objects |= Q(name__icontains=token)

#    return Products.objects.filter(q_objects)