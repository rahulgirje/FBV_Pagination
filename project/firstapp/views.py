from django.shortcuts import render
from .models import User


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def view1(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    template_name = 'firstapp/user.html'
    context = { 'users': users }

    return render(request, template_name,context )
