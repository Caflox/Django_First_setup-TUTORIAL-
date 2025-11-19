from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist

from school_app import models
import json


def hello_world(request):
    return HttpResponse("Hello Peter Cafik sa uci HTTP")

def school(request):
    return HttpResponse("Hello welcome to school")

@csrf_exempt
def list_subjects(request):
    if request.method == "GET":
        subjects=list(models.Subject.objects.values())
        return JsonResponse(subjects, safe=False, status=200)
    elif request.method == "POST":
        subject = request.body

        str= subject.decode("utf-8")

        subject_dict = json.loads(str)
        new_subject = models.Subject(**subject_dict)
        new_subject.save()
        return JsonResponse(subject_dict, status=200)
    else: 
        return HttpResponseNotFound("Sorry this method is not suported")
@csrf_exempt    
def subject_detail(request, pk):
    global subjects

    try:
        subject = models.Subject.objects.get(pk=pk)
        print(subject)
    except ObjectDoesNotExist: 
        return JsonResponse({"status": f"There is no subject with id {pk}"}, status=404)
    if request.method == "GET":
        return JsonResponse(model_to_dict(subject))
    elif request.method == "PUT":
        put_subject = request.body
        str = put_subject.decode("utf-8")
        put_subject_dict = json.loads(str)
        subject.__dict__.update(put_subject_dict)
        subject.save()
        return JsonResponse(put_subject_dict, status = 201)
    elif request.method == 'DELETE':
        subject.delete()
        return HttpResponse(status=204)
    
    # @csrf_exempt
    # def list_teachers(request):
