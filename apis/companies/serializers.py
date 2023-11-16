from rest_framework import serializers
from apis.companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def validate_cnpj(self, value):
        cleaned_cnpj = value.translate(str.maketrans('', '', './-'))
        return cleaned_cnpj
