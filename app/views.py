from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Profile
from .forms import ProfileForm, PostForm
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.


def home(request):
    '''
    It is the view that renders the home page.
    '''
    posts = Post.objects.all()

    return render(request, 'home.html', { 'posts':posts })


@login_required(login_url='/accounts/login/')
def about(request):
    return render(request, 'test.html')

@login_required(login_url='/accounts/login/')
def new_post(request):
    '''
    It creates a new post.
    '''
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = request.user
            post.save()
            return redirect('Home')
    else:
        form = PostForm()

    return render(request, 'post.html', {"form": form})

@login_required(login_url='/accounts/login/')  
def single_post(request,post_id):
    '''
    view function to render a single post on a page
    '''
    post=projo_post.get_single_post(post_id)
    raters=preference.get_rater_users(post.id)
    title=post.title
    form=reviewForm()
    projo_reviews=reviews.project_reviews(post_id)

    desi=post.design
    usabi=post.usability
    conte=post.content
    total=post.total

    rate_desi=(desi/100)*total
    rate_usabi=(usabi/100)*total
    rate_conte=(conte/100)*total
    return render(request, 'single_post.html',{"title":title,"post":post,"form":form,"reviews":projo_reviews,'rate_desi':rate_desi,'rate_usabi':rate_usabi,'rate_conte':rate_conte,'raters':raters})

@login_required(login_url='/accounts/login')
def profile(request):
    '''
    It shows the profile of the logged in user.
    '''
    title = "Profile"
    posts = Post.get_user_posts(request.user.id)
    current_user = request.user

    return render(request, 'profile.html',{'posts':posts})

@login_required(login_url='accounts/login')
def update_profile(request):
    '''
    Function that renders the update profile template and passes the form into it.
    '''
    current_user = request.user
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            Profile.objects.filter(user_id=current_user.id).delete()
            profile = profile_form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect("Profile")
    else:
        profile_form = ProfileForm()

    return render(request, 'update_profile.html', {"profile_form": profile_form})


@login_required(login_url='/accounts/login/')
def other_profiles(request, username):
    o_user = User.objects.get(username=username)
    title = username
    posts = Post.get_user_posts(o_user.id)

    return render(request, 'others_profile.html', {"o_user": o_user, "title": title, "posts": posts})


@login_required(login_url='/accounts/login/')
def update_post(request, post_id):
    '''
    Function that renders the update form for a post.
    '''
    post = Post.get_single_post(post_id)
    instance = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=instance)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = request.user
            post.save()
            return redirect('single_post', post.id)
    else:
        form = PostForm(instance=instance)

    return render(request, 'update_post.html', {"form": form, "post_id": post_id})

@login_required(login_url='/accounts/login/')  
def search(request):
    '''
    view function that searches for projects  
    '''
    if 'search_term' in request.GET and request.GET['search_term']:
        term=request.GET.get('search_term')

        try:      
            projects = Post.search_project(term)      
            message=f'{term}'
            title=term
            return render(request,'search.html',{"message":message,"projects":projects})

        except Post.DoesNotExist:
            message=f'{term}'
            return render(request,'search.html',{"message":message}) 

@login_required(login_url='/accounts/login/')
def logout(request):
    '''
    view function that logout a user
    '''
    logout(request)
    return redirect('home')
