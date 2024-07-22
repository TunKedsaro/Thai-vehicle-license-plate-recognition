from django.shortcuts import render
from django.http import HttpRequest
from django.core.files.storage import FileSystemStorage

from .yolo_model import predict_label

def index(request):
    if request.method == "POST" and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name,image)
        uploaded_file_url = fs.url(filename)
        print("Uploaded file URL:",uploaded_file_url)

        result_label = predict_label(fs.path(filename))
        print("result_label",result_label)

        return render(request,'display_image.html',{
            'uploaded_file_url':uploaded_file_url,
            'result_label':result_label
        })
    return render(request,'index.html')