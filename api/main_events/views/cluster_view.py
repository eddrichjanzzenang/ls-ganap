from main_events.models import Cluster, EventHost
from main_events.serializers import ClusterSerializer, ClusterDetailSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from main_events.pagination import ObjectLimitOffsetPagination, ObjectPageNumberPagination
from rest_framework import status


class ClusterList(APIView):
    """
    get: List all the clusters.
    """
    serializer_class = ClusterSerializer

    def get(self, request, format=None):
        queryset = Cluster.objects.all()
        pagination_class = ObjectPageNumberPagination
        paginator = pagination_class()

        if request.method == 'GET' and 'page' in request.GET:

            page = paginator.paginate_queryset(queryset, request)
            serializer =  ClusterSerializer(page, many=True)
        
            return paginator.get_paginated_response(serializer.data)

        else:
            serializer =  ClusterSerializer(queryset, many=True)
            return Response({"results" : serializer.data})


class ClusterDetail(generics.RetrieveAPIView):
    """
    get: Returns a cluster given its id along with the orgs under it.
    """
    queryset = Cluster.objects.all()
    serializer_class = ClusterDetailSerializer
    pagination_class = ObjectPageNumberPagination
