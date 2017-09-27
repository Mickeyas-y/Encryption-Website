from django.db import models
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Hash import SHA3_512
import base64
import os
import random
import struct


# Create your models here.
class Users(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)


class Post(models.Model):
    def upload_to(instance, filename):
        return '%s/files/%s' % (instance.owner.username, filename)

    postname = models.CharField(max_length=250, null=True)
    Content = models.TextField(max_length=300, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, Users, related_name='+')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    #password = models.CharField(max_length=150, null=True)
    file = models.FileField(upload_to=upload_to, null=True, blank=True)

    #Unicode data - without this * notice change to object in url: 1277.0.0.1:8000/admin/Post
    def getOwner(self):
        return Users.username

    def getFileName(self):
        return self.name

    def encryptfile(in_filename, out_filename = None, chunksize = 64 * 1024):
        secret = get_random_bytes(16)
        if not out_filename:
            out_filename = in_filename + '.enc'

        iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
        encryptor = AES.new(secret, AES.MODE_CBC, iv)
        filesize = os.path.getsize(in_filename)

        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))
                outfile.write(iv)

                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += ' ' * (16 - len(chunk) % 16)

                    outfile.write(encryptor.encrypt(chunk))

class Messages(models.Model):
    def upload_to(instance):
        return 'Messages/%s/%s' % (instance.owner.username)

    title = models.CharField(max_length=100)
    message = models.TextField(max_length=5000)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, Users, related_name='+')

class encMessages(models.Model):
    def upload_to(instance):
        return 'encrypted_messages/%s/%s' % (instance.owner.username)

    title = models.CharField(max_length=100)
    encrypted_message = models.TextField(max_length=7500)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, Users, related_name='+')

#class feedback(models.Model):
