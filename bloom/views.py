from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from rest_framework import permissions, serializers, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ActivitySerializer, OpportunitySerializer, CompanySerializer, ContactSerializer, UserSerializer, UserSerializerWithToken
from .models import Activity, Opportunity, Contact, Company

# Create your views here.

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityView(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    def get_queryset(self, format=None):
        return Activity.objects.filter(owner=self.request.user)
    def post(self, request, format=None):
        if request.method == "POST":
            serializer = UserSerializerWithToken(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OpportunityView(viewsets.ModelViewSet):
    serializer_class = OpportunitySerializer
    def get_queryset(self, format=None):
        return Opportunity.objects.filter(owner=self.request.user)
    def post(self, request, format=None):
        if request.method == "POST":
            serializer = UserSerializerWithToken(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    def get_queryset(self, format=None):
        return Contact.objects.filter(owner=self.request.user)
    def post(self, request, format=None):
        if request.method == "POST":
            serializer = UserSerializerWithToken(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    def get_queryset(self, format=None):
        return Company.objects.filter(owner=self.request.user)
    def post(self, request, format=None):
        if request.method == "POST":
            serializer = UserSerializerWithToken(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)