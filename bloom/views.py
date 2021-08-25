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
    print(request)
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
    queryset = Activity.objects.all()
    
    def post(self, request, format=None):
        if request.method == "POST":
            serializer = UserSerializerWithToken(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "GET":
            data = Activity.objects.all()
            serializer = UserSerializerWithToken(data, context={'request': request}, many=True)
            return Response(serializer.data)

class OpportunityView(viewsets.ModelViewSet):
    serializer_class = OpportunitySerializer
    queryset = Opportunity.objects.all()

    def post(request, format=None):
        if request.method == "POST":
            serializer = UserSerializerWithToken(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "GET":
            data = Opportunity.objects.all()
            serializer = UserSerializerWithToken(data, context={'request': request}, many=True)
            return Response(serializer.data)


class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def post(self, request, format=None):
        if request.method == "POST":
            serializer = UserSerializerWithToken(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "GET":
            data = Contact.objects.all()
            serializer = UserSerializerWithToken(data, context={'request': request}, many=True)
            return Response(serializer.data)

class CompanyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def post(self, request, format=None):
        if request.method == "POST":
            serializer = UserSerializerWithToken(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "GET":
            data = Company.objects.all()
            serializer = UserSerializerWithToken(data, context={'request': request}, many=True)
            return Response(serializer.data)
