from rest_framework.views import APIView
from .models import MultiChoiceUser, MultiChoiceQuestions
from .serializers import GetUserSerializer, GetAllQuestionsSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


class GetUserDetailsView(APIView):
    """Gets the user bio details"""
    serializer_class = GetUserSerializer

    @swagger_auto_schema(
        request_body=GetUserSerializer,
        operation_description="Gets user data.",
        responses={200: 'saved'}
    )
    def post(self, request):
        serializer = GetUserSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        first_name = serializer.validated_data.get("first_name")
        last_name = serializer.validated_data.get("last_name")
        occupation = serializer.validated_data.get("occupation")
        highest_education = serializer.validated_data.get(
            "highest_education"
        )
        phone_number = serializer.validated_data.get("phone_number")
        address = serializer.validated_data.get("address")
        postal_code = serializer.validated_data.get("postal_code")
        marital_status = serializer.validated_data.get("marital_status")
        MultiChoiceUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            occupation=occupation,
            highest_education=highest_education,
            phone_number=phone_number,
            address=address,
            postal_code=postal_code,
            marital_status=marital_status
        )

        return Response(
            "All, good", status=status.HTTP_200_OK
        )


class MultiChoiceQuestionsView(APIView):
    """Gets questions from the database"""
    serializer_class = GetAllQuestionsSerializer

    def get(self, request):
        questions = MultiChoiceQuestions.objects.all()
        serializer = GetAllQuestionsSerializer(questions, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
