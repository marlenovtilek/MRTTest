from django.shortcuts import render, redirect
from django.urls import reverse

from apps.main.models import AnalysisResult


# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def doctor(request):
    return render(request, 'doctor.html')

def departments(request):
    return render(request, 'departments.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def result(request):
    user = request.user

    if not user.is_authenticated:
        return redirect("login")


    analysis_result = user.patient_results.all()
    context = {}

    if analysis_result:
        result_image = analysis_result.first().images.all()
        doctor = analysis_result.first().doctor

        context = {"user": user, "results": analysis_result.first(), "result_image": result_image.first(), "doctor": doctor}
    return render(request, 'result.html', context=context)

# def result_detail(request, result_id):

#     result = AnalysisResult.objects.get(id=result_id)

#     return render(request, "result_detail.html", context={"result": result})