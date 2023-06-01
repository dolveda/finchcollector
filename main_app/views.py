from django.shortcuts import render

finches = [
    {'name': 'Tweety', 'breed': 'House Finch', 'description': 'Loves to trick the cat', 'age': 1},
    {'name': 'Polly', 'breed': 'Purple Finch', 'description': 'Talkative and sarcastic', 'age': 2},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})