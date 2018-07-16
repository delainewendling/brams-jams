# Create your views here.
from rest_framework import viewsets, permissions, status, serializers
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User

class SignUp(APIView):

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # the comma after permissions must stay otherwise an error occurs
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=True, methods=["get"], permission_classes=[permissions.AllowAny])
    def get_user(self, request, pk=None):
        """
        Returns the current user, either logged in or anonymous
        """
        if request.user.is_authenticated:
            user = request.user
            serializer = self.get_serializer(user, many=False)
            return Response(serializer.data)
        else:
           return Response({})