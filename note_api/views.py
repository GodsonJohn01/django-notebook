from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate

from .serializers import SnippetSerializer, SnippetCreateSerializer, SnippetOverViewSerializer
from .models import Snippet, Tag


class SnippetOverView(generics.ListAPIView):
    """
    API to list all snippets
    """
    serializer_class = SnippetOverViewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Snippet.objects.filter(user=user)


class SnippetCreate(generics.GenericAPIView):
    """
    API for creating a new snippet
    """
    serializer_class = SnippetCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.data['title']
        content = serializer.data['content']
        if Tag.objects.filter(title=title).exists():
            return JsonResponse({'message': 'Oops! snippet with the same title already exists.'})
        else:
            tag, _ = Tag.objects.get_or_create(title=title)
            Snippet.objects.create(
                tag=tag, content=content, user=self.request.user)
            return JsonResponse({'message': 'Snippet created sucessfully'})


class SnippetRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API for user retrieving updating and deleting snippet info
    """
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Snippet.objects.filter(user=user)


@csrf_exempt
def signup(request):
    """
    API for user signup
    """
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data['username'], password=data['password'])
            user.save()
            return JsonResponse({'message': 'Sign up successfull'})
        except:
            return JsonResponse({'error': 'Oops! That\'s not a valid username or password!'})
    else:
        return JsonResponse({'error': 'Method not allowed or credentials not provided'})


@csrf_exempt
def login(request):
    """
    API for user login
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request, username=data['username'], password=data['password'])
        if user is not None:
            return JsonResponse({'message': 'Login successfull'})
        else:
            return JsonResponse({'error': 'Invalid username or password'})
    return JsonResponse({'error': 'Method not allowed or Invalid credentials'})
    