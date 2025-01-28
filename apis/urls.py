from django.urls import path
from .views import TherapistDataView

urlpatterns = [
    path('therapists/', TherapistDataView.as_view(), name='therapist-data'),
]
