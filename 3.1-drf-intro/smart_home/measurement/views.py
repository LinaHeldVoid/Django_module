# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import \
    ListCreateAPIView, \
    RetrieveUpdateAPIView, \
    CreateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import \
    SensorSerializer, \
    SensorDetailSerializer, \
    MeasurementDetailSerializer, \
    MeasurementSerializer


class SensorCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_field = 'id'


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementDetailSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        sensor = self.get_object()
        serializer = self.get_serializer(sensor)
        data = serializer.data

        measurement = Measurement.objects.filter(sensor=sensor)
        measurement_serializer = MeasurementSerializer(measurement, many=True)
        data['measurements'] = measurement_serializer.data

        return Response(data)
