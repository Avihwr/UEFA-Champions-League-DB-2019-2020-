from django.shortcuts import render
from .models import *


# Create your views here.


def home(request):
    topplayers = Player.objects.order_by('-Overall')[0:5]
    topteams = Club.objects.order_by('-Goals')[0:5]
    topscorers = Player.objects.order_by('-Goals')[0:5]
    mostvaluableplayer = Player.objects.order_by('-Market_Value')[0:5]
    mostvaluableteam = Club.objects.order_by('-Market_Value')[0:5]
    manager = Manager.objects.all()[0:5]
    context = {
        'topplayers': topplayers,
        'topteams': topteams,
        'topscorers': topscorers,
        'managers': manager,
        'mostvaluableplayers': mostvaluableplayer,
        'mostvaluableteams': mostvaluableteam
    }
    return render(request, 'index.html', context)


def players(request):
    player = Player.objects.all()
    teamss = AllTeams.objects.all()
    context = {'players': player, 'teams': teamss}
    return render(request, 'players.html', context)


def teams(request):
    team = Club.objects.all()
    context = {'teams': team}
    return render(request, 'teams.html', context)


def top_scorer(request):
    player = Player.objects.all().order_by('-Goals')
    team = AllTeams.objects.all()
    context = {'players': player, 'teams': team}
    return render(request, 'players.html', context)


def managers(request):
    team = Club.objects.all()
    context = {'teams': team}
    return render(request, 'managers.html', context)


def mvp(request):
    mvps = Player.objects.all().order_by('-Market_Value')
    context = {'players': mvps}
    return render(request, 'mostvaluableplayer.html', context)


def mvt(request):
    mvts = Club.objects.all().order_by('-Market_Value')
    context = {'teams': mvts}
    return render(request, 'mostvaluableteams.html', context)

# def search(request):
#     query = request.GET['query']
#     if len(query) > 80:
#         queryposts = Blog.objects.none()
#     else:
#         querypostsTitle = Blog.objects.filter(title__icontains=query)
#         querypostsContent = Blog.objects.filter(content__icontains=query)
#         querypostsTC = querypostsTitle.union(querypostsContent)
#         querypostsAuthor = Blog.objects.filter(username__icontains=query)
#         querypostsExcerpt = Blog.objects.filter(excerpt_type__excerpt__icontains=query)
#         queryposts1 = querypostsAuthor.union(querypostsTC)
#         queryposts = queryposts1.union(querypostsExcerpt)
#
#     if queryposts.count() == 0:
#         messages.warning(request, "No Search Results Found. Please Refine Your Query")
#     context = {'QueryPosts': queryposts, 'query': query}
#     return render(request, 'search.html', context)