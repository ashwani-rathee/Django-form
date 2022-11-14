from django.shortcuts import render, HttpResponse
from .forms import CourseForm

def UploadImage(request):
    if request.method == 'POST':
        form = CourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The image saved successfully')
    else:
        form = CourseForm()
        context = {
            'form':form,
        }
    return render(request, 'upload.html', context)
