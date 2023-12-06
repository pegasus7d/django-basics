from calendar import month
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse
# from django.template.loader import render_to_string

MONTH_NAME_CHALLENGES = {
    'january': 'Eat no meat for the entire month',
    'february': 'Walk for at least 20 minutes every day',
    'march': 'Read a book every week',
    'april': 'Practice meditation for 10 minutes daily',
    'may': 'Learn a new language for 15 minutes daily',
    'june': 'Try a new hobby or activity each week',
    'july': 'Drink at least 8 glasses of water every day',
    'august': 'Take a break from social media for the entire month',
    'september': 'Exercise for at least 30 minutes every day',
    'october': 'Write a journal entry every day',
    'november': 'Express gratitude daily',
    'december': 'Donate to a charity or volunteer your time',
    # 'december': None
}


def index(request):
    list_items=""
    months=list(MONTH_NAME_CHALLENGES.keys())
    # for month in months:
    #     capitalized_month=month.capitalize()
    #     month_path=reverse("month-challenge",args=[month])
    #     list_items+=f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data=f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    return render(request,"challenges/index.html",{
        "months":months
    })

def monthly_challenge_by_number(request, month):
    months=list(MONTH_NAME_CHALLENGES.keys())
    if month>len(months):
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    forward_month=months[month-1]
    redirect_path=reverse("month-challenge",args=[forward_month])
    return HttpResponseRedirect(redirect_path)
    #return HttpResponseRedirect('/challenges/'+forward_month)

def monthly_challenge(request, month):
    month_lower = month.lower()
    challenge_text = MONTH_NAME_CHALLENGES.get(month_lower)
    # response_data=f"<h1>{challenge_text}</h1>"
    # response_data=render_to_string("challenges/challenge.html")
    if challenge_text :
        return render(request,"challenges/challenge.html",{
            "text":challenge_text,
            "month_name":month,
        })
    else:
        raise Http404("404.html")
