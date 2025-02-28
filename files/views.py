# from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from .models import File
from .serializers import FileSerializer, userSerializer
from .forms import UploadForm


# Create your views here.
@api_view(['POST'])
def register(request):
     serializer = userSerializer(data = request.data)
     if serializer.is_valid():
          serializer.save()
          return Response(status = status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def files(request, format=None):
    if request.method == 'GET':
        data = request.user.file_set.all()
        serializer = FileSerializer(data, many=True)
        return Response({'files': serializer.data})
        
    elif request.method == 'POST':
        serializer = FileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def file(request, file_id):
    try:
        data = request.user.file_set.get(pk=file_id) 
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FileSerializer(data)
        return Response({'file': serializer.data})
    
    elif request.method == 'PUT':
        name = request.POST.get('name')
        file_type = request.POST.get('type')
        data = File.objects.get(pk=file_id)
        print(name, file_type, data)

        if data:
                if name:
                    data.name = name
                if file_type:
                    data.file_type = file_type
                data.save()
                return redirect(files)
        else:
                return redirect(files)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   
        













# 


































# /////////////////////////

# def file(request, file_id):
#     f = File.objects.get(pk = file_id)
#     serializer = FileSerializer(f)
#     return JsonResponse({"file": serializer.data})

# def files(request):
#     files = File.objects.all()
#     return render(request, "files/files.html", {"files":files})

# def file(request, file_id):
#     f = File.objects.get(pk = file_id)
#     if f is not None:
#         return render(request, "files/files.html", {"files":f})
#     else:
#         return Http404("file does not exit")

# def edit(request, file_id):
#     name = request.POST.get('name')
#     file_type = request.POST.get('type')
#     f = File.objects.get(pk=file_id)
#     print(name, file_type, f)

#     if f:
#         if name:
#             f.name = name
#         if file_type:
#             f.file_type = file_type
#         f.save()
#         return redirect(files)
#     else:
#         return redirect(files)

# def delete(request, file_id):
#     f = File.objects.get(pk=file_id)   
#     if f:
#         f.delete()
#     return redirect(files)

# def file(request, file_id):
#     try:
#         f = File.objects.get(pk = file_id, format= None)
#     except File.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)
#     serializer = FileSerializer(f)
#     return JsonResponse({"file": serializer.data}, status=status.HTTP_200_OK)


# def files(request):
#     f = File.objects.all()
#     serializer = FileSerializer(f, many = True)
#     return JsonResponse(serializer.data, safe=False)
#     return JsonResponse({"files": serializer.data})




# def files(request):
#     f = File.objects.all()
#     return render(request, 'files/files.html', {'files': f, 'form': UploadForm})
# /////////////////////////////////////
# @api_view(['GET', 'PUT', 'DELETE'])
# def files(request,  file_id, format = None):
#     if request.method == 'GET':
#         try:
#             data = File.objects.get(pk = file_id, format= None)
#         except File.DoesNotExist:
#             return Response(status = status.HTTP_404_NOT_FOUND)
#         serializer = FileSerializer(data)
#         return JsonResponse({"file": serializer.data}, status=status.HTTP_200_OK)
    

#     elif request.method == 'PATCH':
#         serializer = FileSerializer(data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
#     elif request.method == 'PUT':
#         serializer = FileSerializer(data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 # try:
        #         f = File.objects.get(pk = file_id)
        # except File.DoesNotExist:
        #         return Response(status = status.HTTP_404_NOT_FOUND)
        # serializer = FileSerializer(f)
        # return JsonResponse({"file": serializer.data}, status=status.HTTP_200_OK)


# name = request.POST.get('name')
        # file_type = request.POST.get('type')
        # data = File.objects.get(pk=file_id)
        # print(name, file_type, data)

        # if data:
        #     if name:
        #         data.name = name
        #     if file:
        #         data.file_type = file_type
        #     data.save()
        #     return redirect(File)
        # else:
        #     return redirect(File)

