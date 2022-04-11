from rest_framework import generics
from rest_framework import viewsets
# Create your views here.
# class BaseListView(generics.ListCreateAPIView):
#     def __init__(self, model, serializer):
#         queryset=model.objects.all()
#         serializer_class= serializer
    
# class BaseDetailView(generics.RetrieveUpdateDestroyAPIView):
#     def __init__(self, model, serializer):
#         queryset=model.objects.all()
#         serializer_class= serializer



class BaseView(viewsets.ModelViewSet):
    def __init__(self, model, serializer):
        self.queryset = model.objects.all()
        self.serializer_class = serializer