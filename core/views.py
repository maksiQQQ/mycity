from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from .serializers import ProposialListSerializer, ProposialCreateSerializer, \
    ProposialSerializer
from .models import Proposial


class ProposialListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        proposials = Proposial.objects.all()
        proposials_json = ProposialListSerializer(proposials, many=True)
        return Response(data=proposials_json.data)


class ProposialCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        serializer = ProposialCreateSerializer(data=data)
        if serializer.is_valid():
            proposial = serializer.save()
            json_data = ProposialSerializer(instance=proposial)
            return Response(json_data.data, 201)
        return Response(
            data={
                "message": "Data not valid",
                "errors": serializer.errors
            },
            status=400
        )

class ProposialRetrieveAPIView(RetrieveAPIView):
    queryset = Proposial.objects.all()
    serializer_class = ProposialSerializer