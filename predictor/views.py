from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from predictor.learner import Learner
import os


class PredictorView(APIView):

  def post(self, request):
    brand = request.data['brand']
    model = request.data['name']
    kms = int(request.data['kms'])
    license = request.data['license']
    year = int(request.data['year'])
    capacity = int(request.data['capacity'])
    cycle_type = request.data['cycleType']
    print(brand, model, kms, license, year, capacity, cycle_type)
    learner = Learner()
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'data/motoDatasetFinal.csv')

    learner.set_encoder(file_path)
    price = learner.train_and_predict(file_path, brand, model, kms, license, year, capacity, cycle_type)

    return Response(price, status=status.HTTP_200_OK)