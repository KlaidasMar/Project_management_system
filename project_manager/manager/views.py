from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import User
from django.core.paginator import Paginator
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.db.models import Q
from .models import Projektas, Klientas, Darbuotojas, Darbas, Saskaita


def index(request):
    num_projects = Projektas.objects.all().count()
    num_clients = Klientas.objects.all().count()
    num_workers = Darbuotojas.objects.all().count()

    context = {
        'num_projects': num_projects,
        'num_clients': num_clients,
        'num_workers': num_workers,
    }

    return render(request, 'index.html', context=context)


# def search(request):
#     query = request.GET.get('query')
#     search_results = Projektas.objects.filter(Q(pavadinimas__icontains='ref') | Q(klientas__icontains='ref'))
#     return render(request, 'search.html', {'projects': search_results, 'query': query})

def search(request):
    query = request.GET.get('query')
    search_results = Projektas.objects.filter(Q(pavadinimas__icontains=query) | Q(vadovas__icontains=query))
    context = {
        'projects': search_results,
        'query': query,
    }
    return render(request, 'search.html', context=context)


def projects(request):
    paginator = Paginator(Projektas.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_projects = paginator.get_page(page_number)
    context = {
        'projects': paged_projects
    }
    return render(request, 'projects.html', context=context)


def project(request, project_id):
    single_project = get_object_or_404(Projektas, pk=project_id)
    return render(request, 'project.html', {'project': single_project})


def clients(request):
    clients = Klientas.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'clients.html', context=context)


def client(request, client_id):
    single_client = get_object_or_404(Klientas, pk=client_id)
    return render(request, 'client.html', {'client': single_client})