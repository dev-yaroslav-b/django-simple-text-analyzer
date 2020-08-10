import re
from django.shortcuts import redirect, render
from django.views import generic

from .forms import PostForm
from .models import Post


class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all().order_by('-count')


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            words = form.data['word']
            words = re.sub(r'[^A-Za-z0-9 ]+', '', words)
            words = re.sub(' +', ' ', words)
            words = words.split()

            for w in words:
                word_in_db = Post.objects.filter(word=w).first()
                if word_in_db:
                    word_in_db.count += 1
                    word_in_db.save()
                else:
                    new_post = Post(word=w)
                    new_post.save()

            return redirect('/')
    else:
        form = PostForm()

    template = 'pages/create_post.html'
    forms = {
        'form': form
    }
    return render(request, template, forms)
