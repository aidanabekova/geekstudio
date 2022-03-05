from rest_framework import serializers
from blog.models import Master, Review, Procedure, Branch
from rest_framework.exceptions import ValidationError


class MasterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text value'.split()


class ProcedureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = 'id name description price'.split()


class BranchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class ProcedureCreatedSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(min_length=10, max_length=200)
    price = serializers.IntegerField()
    master = MasterSerializers(many=True)

    def validate_name(self, name):
        procedure = Procedure.objects.filter(name=name)
        if procedure:
            raise ValidationError('Prosedure already exists!')
        return name
