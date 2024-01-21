from django.shortcuts import render,redirect
from django.contrib import messages
from . models import Post,Catagory, Comments
from . forms import Post_Form,SignupForm,CommetnsForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def Blog_Post(request,catagory_slug=None):
    cate=Catagory.objects.all()
    post=Post.objects.all().order_by('-id')

    if catagory_slug is not None:
        categoryes=Catagory.objects.get(slug=catagory_slug)
        post=Post.objects.filter(catagory=categoryes)

    context={'post':post,'cate':cate}
    return render (request,'home.html',context)


def Post_details(request,id):
    post_details=Post.objects.get(id=id)
    all_comment=Comments.objects.filter(post=post_details)
    if request.method=='POST':
        form=CommetnsForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.instance.post=post_details
            form.save()
            form=CommetnsForm()
    else:
        form=CommetnsForm()
    context={'post_details':post_details,'fm':form,'all_comment':all_comment}
    return render(request,'post_details.html',context)
@login_required
def Add_Post(request):
    if request.method == 'POST':
        form=Post_Form(request.POST,request.FILES)
        if form.is_valid():
            form.instance.author=request.user
            form.save()
            
            
            form=Post_Form()
            messages.success(request,'create post success')

    else:
        form=Post_Form()
    context={'fm':form}
    return render(request,'add_post.html',context)





def SignupUser(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form=SignupForm(request.POST)
            if form.is_valid():
                messages.success(request,'Accunt create successfull')
                form.save()
                form=SignupForm()
        else:
            form=SignupForm()
        context={'fm':form}

        return render(request,'signup.html',context)
    else:
        return redirect('profile')


def Login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                passwords=form.cleaned_data['password']
                user=authenticate(username=uname,password=passwords)
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            form=AuthenticationForm()
        context={"fm":form}
        return render(request,'login.html',context)
    else:
        return redirect('profile')

def Logut(request):
    logout(request)
    return redirect('login')

@login_required
def Profile(request):
    return render(request,'profile.html')


@login_required
def Cahnge_passwords(request):
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user)
            messages.success(request,'password change successfull')
            form=PasswordChangeForm(request.user)
    else:
        form=PasswordChangeForm(request.user)
    context={'fm':form}
    return render(request,'changepasswithold.html',context)



@login_required
def Cahnge_passwords_without_old_pass(request):
    if request.method=='POST':
        form=SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user)
            messages.success(request,'password change successfull')
            form=SetPasswordForm(request.user)
    else:
        form=SetPasswordForm(request.user)
    context={'fm':form}
    return render(request,'change_pass_with_out_old_pass.html',context)



