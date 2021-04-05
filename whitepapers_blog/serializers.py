from whitepapers_blog.models import WhitePapers
from rest_framework import serializers

class WhitePapersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=WhitePapers
        fields=('name','symbol','category','content')