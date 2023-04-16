from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
    	'author': 'Администратор',
    	'title': 'Это первый пост',
    	'content': 'Содержание первого поста.',
    	'date_posted': '12 мая, 2022'
	},
	{
    	'author': 'Пользователь',
    	'title': 'Это второй пост',
    	'content': 'Подробное содержание второго поста.',
    	'date_posted': '13 мая, 2022'
	}
]
# Create your views here.
def home(request):
    ctx = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', ctx)


def about(request):
    return render(request, 'blog/about.html', {'title': 'О клубе Python Bytes'})
