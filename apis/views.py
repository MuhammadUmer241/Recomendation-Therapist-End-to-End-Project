from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Therapist
from .serializer import TherapistSerializer

# Generic View to handle both POST and GET for Therapist data
class TherapistDataView(GenericAPIView):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer

    def get(self, request):
        """
        Retrieve all therapist data.
        """
        therapists = self.get_queryset()
        serializer = self.get_serializer(therapists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Save new therapist data.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Therapist data saved successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
