from django.shortcuts import render

posts = [
    {
        "author": "behren",
        "title": "Post 1",
        "content": "Liste der VHV-Stages",
        "date_posted": "9. März 2021",
    },
    {
        "author": "schadb1",
        "title": "Post 2",
        "content": "Liste der BVA-Stages",
        "date_posted": "10. März 2021",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/stages.html", {"title": "Stages"})
