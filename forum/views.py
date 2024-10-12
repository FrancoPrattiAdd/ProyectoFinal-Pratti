from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator

# Vista para listar todos los posts
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  
    paginator = Paginator(posts, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'forum/forum_list.html', {'page_obj': page_obj})

# Vista para ver el detalle de un post específico
def post_detalle(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()
    return render(request, 'forum/detalle_post.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

# Vista para crear un nuevo post 
@login_required
def crea_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'forum/crear_post.html', {'form': form})

# Vista para editar un post existente 
@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('post_detail', post_id=post.id)  

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'forum/post_form.html', {'form': form, 'post': post})

# Vista para eliminar un post 
@login_required
def borrar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author:
        post.delete()
        return redirect('post_list')
    return redirect('post_detail', post_id=post.id)
