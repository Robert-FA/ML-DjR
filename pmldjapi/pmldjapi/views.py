from rest_framework.decorators import api_view
from rest_framework.response import Response
import pickle

@api_view(['POST'])
def predict(request):
    # Load the machine learning model from file
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Get the data from the request
    data = request.data

    # Make a prediction using the machine learning model
    prediction = model.predict(data)

    # Return the prediction as a JSON response
    return Response({'prediction': prediction.tolist()})
