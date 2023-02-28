from rest_framework import status, generics
from rest_framework.response import Response
from .serializer import *
from datetime import datetime, timedelta
from rest_framework.decorators import api_view

# Create your views here.
class ClockPunchInView(generics.GenericAPIView):
    serializer_class = EmployeeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "note": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST'])
def login(request):
    data = request.data
    now = datetime.now()
    timing_objs = EmployeeDitels.objects.filter(id=data['ids'])
    serializer = EmployeeSerializer(timing_objs, many=True)
    obj = EmployeeDitels.objects.get(id=serializer.data[0]['id'])
    if serializer.data[0]["punch_in"] == True:
        seri = EmployeeSerializer(obj, data={'punch_in': False},
                                  partial=True)
        if seri.is_valid():
            seri.save()
            statu = "punch_in"
                # serializer.save()
    else :
        seri = EmployeeSerializer(obj, data={'punch_in': False},
                                  partial=True)
        if seri.is_valid():
            seri.save()
            statu = "punch_Out"
    return Response({"status": statu, "note": data}, status=status.HTTP_201_CREATED)
