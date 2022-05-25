from django.shortcuts import render
from django.http import HttpResponse

#Dummy dat - will be removed 

cow_list = [
    {
        "id": 1,
        "name": "Daisy", 
        "age" : 3
    },
    {
        "id": 2,
        "name": "Cow", 
        "age" : 1},
    {
        "id": 3,
        "name": "Lucy", 
        "age" : 7
    }
]

# Create your views here.

def index(request):

    return HttpResponse("""
    <h1>Livestock</h1>
    <em>where animals are things</em>
    """)

def about(request):

    return HttpResponse("""
    <h1>About</h1>
    <p>Sunset Oaks Farm is a happy community of independently-minded cows</p>
    """)

def shop(request):

    return HttpResponse("""
    <h1>Shop</h1>
    <p>Welcome to Sunset Oaks Farm shop where we sell everything except animal flesh</p>
    """)


def cows(request):
    data = {
        "cows": cow_list
    }
    return render(request, 'cows.html', data)

    # return HttpResponse(f"""
    # <h1>Cow list</h1>
    # <h2>Welcome to Sunset Oaks Farm Cows.<h2>
    # <p>Currently, we have {len(cow_list)} cows.</p>
    # """)

def cow(request, id):

    cowsen_one = list(filter(lambda c: c["id"] == id, cow_list))[0]

    return HttpResponse(f"""
    <h1>Cow Profile: {cowsen_one['name']}</h1>
    <p>{cowsen_one['name']} is {cowsen_one['age']} years old.</p>
    """)
