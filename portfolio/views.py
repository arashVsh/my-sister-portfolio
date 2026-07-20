from django.shortcuts import render

def home(request):
    context = {
        "photos": [f"portfolio/images/gallery/{i}.jpg" for i in range(1, 9)],
        "videos": [f"portfolio/videos/{i}.mp4" for i in range(1, 4)],
    }
    return render(request, "portfolio/home.html", context)
