from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from spoty.models import song, reviews

# Create your views here.
def index(request):
    return render(request, 'welcome.html', {'songs': song.objects.all()})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
            
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def search(request):
    if request.method == 'POST':
        search= request.POST['search']
        songs = song.objects.all()
        found_songs = song.objects.filter(title__contains=search)
        found_songs = found_songs | song.objects.filter(artist__contains=search)
        return render(request, 'welcome.html', {'songs': songs, 'found_songs': found_songs})
    else:
        return render(request, 'welcome.html')

def review(request, pk):
    if request.method == 'POST':
        text = request.POST['review']
        rating = request.POST['rating']
        user = request.user
        song_id = pk
        reviews.objects.create(song=song.objects.get(id=song_id), text=text, user=user, rating=rating)

        song_to_update = song.objects.get(id=song_id)
        song_to_update.ranking = (song_to_update.ranking + float(rating)) / 2
        song_to_update.save()
        return redirect('song_page', pk=pk)
    else:
        return render(request, 'add_review.html', {'song': song.objects.get(id=pk)})

def post(request, pk):
    return render(request, 'song_view.html', {'song': song.objects.get(id=pk), 'song_reviews': reviews.objects.filter(song=song.objects.get(id=pk))})