from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import View
from .forms import RegForm, usrPost, usrMessage, usrEncMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django import forms

from django.core import validators
from django.core.validators import ValidationError
from django.core.files.uploadhandler import FileUploadHandler
from django.core.files import uploadedfile
from django.core.files import File
from Cryptodome.Hash import SHA3_512
from Cryptodome.Random import get_random_bytes
from .models import Users
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import loader


from .models import Post, Messages, encMessages
import base64
import os, random, struct
# Create your views here.

from django.http import HttpResponse

@csrf_protect
def index(request):
    if request.user.is_authenticated():
        userPosts_list = Post.objects.filter(owner = request.user)
        userMessages_list = Messages.objects.filter(owner = request.user)
        userEncMessages_list = encMessages.objects.filter(owner = request.user)

        paginator = Paginator(userPosts_list, 3)  # Show 3 contacts per page
        page = request.GET.get('page1')

        try:
            userPosts = paginator.page(page)

        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            userPosts = paginator.page(1)

        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            userPosts = paginator.page(paginator.num_pages)

########################## end of post pagination#################################

        paginator = Paginator(userMessages_list, 2)

        page = request.GET.get('page2')

        try:
            userMessages = paginator.page(page)

        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            userMessages = paginator.page(1)

        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            userMessages = paginator.page(paginator.num_pages)

########################## end of Message pagination#################################

        paginator = Paginator(userEncMessages_list, 2)

        page = request.GET.get('page3')

        try:
            userEncMessages = paginator.page(page)

        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            userEncMessages = paginator.page(1)

        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            userEncMessages = paginator.page(paginator.num_pages)


        context = {
            "posts": userPosts,
            "messages": userMessages,
            "encmessages": userEncMessages,
            #"results": results,
        }

    else:
        context = {

        }

    return render(request, 'users/index.html', context)

@csrf_protect
def delete_m(request, id):
    delete_m_by_id = Messages.objects.get(id=id).delete()
    return render(request, 'users/index.html')

@csrf_protect
def delete_em(request, id):
    delete_em_by_id = encMessages.objects.get(id=id).delete()
    return render(request, 'users/index.html')

@csrf_protect
def delete_f(request, id):
    delete_f_by_id = Post.objects.get(id=id).delete()
    return render(request, 'users/index.html')

@csrf_protect
def guidepage(request):
    return render(request, 'users/guidepage.html')

@csrf_protect
def register(request):
    return render(request, 'users/registration_form.html')

@csrf_protect
def signin(request):
    return render(request, 'users/login_form.html')

@login_required
def signout(request):
    logout(request)
    return render(request, 'users/index.html')

@login_required
def decryptfile(request):
    return render(request, 'users/decrypt_file.html')

#@csrf_protect
#def textencryption(request):
#    text_box_value = request.GET['text_box']
#    print(text_box_value)

#    return render(request, 'users/encrypt_text_form.html')

@login_required
def encrypttext(request):
    form = usrEncMessage(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner = request.user
        instance.save()
    context = {
        "form": form,
    }
    return render(request, 'users/encrypt_text_form.html', context)

@login_required
def decrypttext(request):
    return render(request, 'users/decrypt_text_form.html')

@login_required
def decryptmsg(request, oid):
    msgid = encMessages.object.filter(id=oid).first()
    context={
        'msgid':msgid,
    }
    return render(request, 'users/decrypt_text_form.html',context)

@login_required
def post_create(request):
    form = usrPost(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner = request.user
        #instance.password = request.POST.password
        #instance.password = SHA3_512.new(instance.password).encoded("latin-1")
        #instance.file = request.FILES
        #in_filename = request.FILES['file']
        #out_filename = in_filename

        #with open(in_filename, 'rb') as in_file, open(out_filename, 'wb') as out_file:
         #   instance.file=Post.encryptfile(in_file, out_file)

        instance.save()
        messages.success(request, "Successfully Created")
    context = {
        "form": form,
    }
    return render(request, "users/user_post_file.html", context)

@login_required
def message_create(request):
    form = usrMessage(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner = request.user
        instance.save()
        messages.success(request, "Successfully Created")
    context = {
        "form": form,
    }
    return render(request, "users/user_post_messages.html", context)


class UserRegFormView(View):
    form_class = RegForm
    template_name = 'users/registration_form.html'

    #display my form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            cnfpword = form.cleaned_data['cnfpassword']

            if password and cnfpword:
                if password != cnfpword:
                    #messages.success(request, "Successfully Created")
                    message="Confirmation error, your passwords do not match."


                    #return render(request, 'users/registration_form.html', {'form': form}, message)
                    #raise forms.ValidationError("Password fields do not match!")
                    return render(request, "users/Error.html", {'Error': message})


                user.set_password(password)
                user.save()

            # returns User objects if credentials are correct
                user = authenticate(username=username, password=password)

                #if user is not None:

                    #if user.is_active:
                    #login(request, user)
                        #return redirect('users:signin')

        return render(request, self.template_name, {'form': form})


class UserLogFormView(View):
    form_class = RegForm
    template_name = 'users/login_form.html'

    #display my form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        #if form.is_valid():#user = form.save(commit=False)

        username = request.POST['username']
        password = request.POST['password']
        #user.save()
        # returns User objects if credentials are correct

        user = authenticate(username=username, password=password)

        if not user or not user.is_active:
            message = "Your username and passwords do not match!"
            return render(request, "users/Error.html", {'Error': message})
        else:
            if user:
                if user.is_active:
                    login(request, user)
                    if request.user.is_authenticated():
                        messages.info(request, "Welcome " + user.username)
                        return redirect('users:index')
                    #else: # to display password incorrect
                        #message = "Your username and passwords do not match!"
                    #return render(request, "users/Error.html", {'Error': message})

        return render(request, self.template_name, {'form': form})