from django.http import HttpResponse, JsonResponse, Http404
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Graphic
from .serializers import GraphicSerializer

#
# @api_view(['GET', 'POST'])
# def graphic_list(request):
#     """
#     List all graphics, or create a new graphic.
#     """
#     if request.method == 'GET':
#         snippets = Graphic.objects.all()
#         serializer = GraphicSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = GraphicSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_200_OK)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# @csrf_exempt
# def graphic_detail(request, pk):
#     """
#     Retrieve, update or delete a graphic.
#     """
#     try:
#         snippet = Graphic.objects.get(pk=pk)
#     except Graphic.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = GraphicSerializer(snippet)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = GraphicSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# class GraphicDetail(APIView):
#     """
#     Retrieve, update or delete a graphic instance.
#     """
#
#     def get_object(self, pk):
#         try:
#             return Graphic.objects.get(pk=pk)
#         except Graphic.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = GraphicSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = GraphicSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class GraphicList(APIView):
#     """
#     List all snippets, or create a new graphic.
#     """
#
#     def get(self, request, format=None):
#         snippets = Graphic.objects.all()
#         serializer = GraphicSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = GraphicSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .models import Graphic
from .serializers import GraphicSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class GraphicList(generics.ListCreateAPIView):
    queryset = Graphic.objects.all()
    serializer_class = GraphicSerializer
    permission_classes = [IsAuthenticated]


class GraphicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Graphic.objects.all()
    serializer_class = GraphicSerializer
