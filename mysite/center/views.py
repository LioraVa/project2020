from django.shortcuts import render
# Create your views here.

Medical_Institutes = [
    {
        'Institute':'Maccabi',
        'city': 'beer sheva',
        'phone': '088888888',
        'date_posted': 'August 26, 2017'
    },
    {
        'Institute': 'Maccabi',
        'city': 'beer sheva',
        'phone': '088888888',
        'date_posted': 'August 2, 2015'
    },
    {
        'Institute': 'Maccabi',
        'city': 'beer sheva',
        'phone': '088888888',
        'date_posted': 'August 21, 2011'
    }
]
def home(request):
    context = {
        'Medical_Institutes': Medical_Institutes
    }
    return render(request, 'center/home.html', context)

def about(request):
    # return render(request, 'center/about.html')
    return render(request, 'center/about.html', {'title': 'About'})
