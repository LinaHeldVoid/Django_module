from django.urls import path

from .views import SensorCreateView, SensorUpdateView, MeasurementView, SensorDetailView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorCreateView.as_view()),
    path('sensors/<id>/', SensorUpdateView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensor/<id>', SensorDetailView.as_view()),
]
