from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .models import Book
from .models import Review
# from .models import *

# Create your views here.
# Login Section

def new(req):
  return render(req, 'belt_reviewer2_app/new.html')

def create(req):
  errors = User.objects.validate(req.POST)
  if errors:
    for error in errors:
      messages.error(req, error)
    return redirect('/new')
  # create and login user
  user = User.objects.create_user(req.POST)
  # req.session['first_name'] = req.POST['first_name']
  req.session['user_id'] = user.id #trying this instead
  messages.success(req, "Successfully registered!")
  return redirect('/success')

def login(req):
  valid, result = User.objects.check_login(req.POST)
  if not valid:
    for error in result:
      messages.error(req, error)
    return redirect('/new')

  req.session['first_name'] = result.first_name
  # req.session['id'] = User.objects.get(id)
  messages.success(req, "Successfully logged in!")
  return redirect('/success')

def logout(req):
  # pass
  req.session.clear()
  return redirect('/new')

def success(req):
  context = {
        "users" : User.objects.all(),
  }
  
  return render(req, 'belt_reviewer2_app/index.html', context)

# Adding Books/Reviews Section



def add(req):
  return render(req, 'belt_reviewer2_app/add.html')

def createbook(req):
  

  # i am here.

  #attach the created object to the variable book. then skip to line 69
  book = Book.objects.create(
  book_title=req.POST["book_title"],
  author = req.POST["author"]
  )

  book = Book.objects.get(
  book_title=req.POST['book_title'] 
  )

  book.review.create(
  review=req.POST['review'], rating = req.POST['rating'], 
  id=req.session['user_id']
  )




  # review = Review.objects.create(
  # review = req.POST["review"], #Missing data from page
  # rating = req.POST["rating"], #Missing data from page
  # book = book, #book is the object above
  # user = User.objects.get(id=req.session['user_id']) #this is the reviews.user from the model
  # )


  #line 69 get the id and stringify it for the url
  string = str(book.id)
  #add the string variable to the redirect route
  return redirect('/'+ string +'/show')

def showbook(req):
  context = {
    "books" : Book.objects.all(),
    "reviews" : Review.objects.all() 
  }
  return render(req, 'belt_reviewer2_app/createbook.html', context)


def show(request, id):
    context = {
        "book" : Book.objects.get(id=id),
    }
    return render(request, 'belt_reviewer2_app/createbook.html', context)
