from rest_framework import response, views
from .serializers import *
from .models import *
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated


class ProductsAdminView(views.APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk=None):
        if pk:
            qs = Clothing.objects.get(pk=pk)
            serializer = ClothingSerializer(qs)
            return response.Response(serializer.data)
        else:
            qs = Clothing.objects.all()
            serializer = ClothingSerializer(qs, many=True)
            return response.Response(serializer.data)

    def post(self, request, pk=None):
        serializer = ClothingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def put(self, request, pk=None):
        qs = self.get_object(pk)
        serializer = ClothingSerializer(qs)
        if serializer.is_valid():
            serializer.save()
            return response.Response(data=serializer.data)
        return response.Response(data='Wrong parameters')

    def delete(self, request, pk=None):
        if pk:
            try:
                the_clothing = Clothing.objects.get(pk=pk)
                the_clothing.delete()
                return JsonResponse({'message': 'the specified clothing deleted!'})
            except:
                return HttpResponseNotFound('Sorry!')
        else:
            return HttpResponseNotFound('Give us a pk!')
