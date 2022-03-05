from blog.models import Master, Review, Procedure, Branch
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from blog import serializers


class MasterListCreateAPIview(ListCreateAPIView):
    queryset = Master.objects.all()
    serializer_class = serializers.MasterSerializers
    pagination_class = PageNumberPagination


class MasterDetailUpdateDeleteAPIview(RetrieveUpdateDestroyAPIView):
    queryset = Master.objects.all()
    serializer_class = serializers.MasterSerializers
    lookup_field = 'id'


class ProcedureListCreateAPIview(ListCreateAPIView):
    queryset = Procedure.objects.all()
    serializer_class = serializers.ProcedureCreatedSerializer
    pagination_class = PageNumberPagination


class ProcedureDetailUpdateDeleteAPIview(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializers
    lookup_field = 'id'


class BranchListCreateAPIview(ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = serializers.BranchSerializers
    pagination_class = PageNumberPagination


class ReviewListCreateAPIview(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializers
    pagination_class = PageNumberPagination


