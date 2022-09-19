from rest_framework import serializers
from .models import Lectures, Lecture_Image
from accounts.models import User


#Lectuer_image 시리얼라이저 추가
class LectuerImageSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(use_url=True)
    
    class Meta:
        model=Lecture_Image
        fields=['image']

class LecturesSerializer(serializers.ModelSerializer):
    # 강의 수강 학생 Many To Many Field
    enroll_students = serializers.SlugRelatedField(
        many=True,
        slug_field="nickname", 
        queryset = User.objects.all(),
        #write_only =True
        read_only = False
        )
    
    # 강의 좋아요 누른 회원 Many To Many Field
    like_members = serializers.SlugRelatedField(
        many=True,
        slug_field="nickname", 
        queryset = User.objects.all(),
        #write_only =True
        read_only = False
        )
    
    #images필드 추가
    images=serializers.SerializerMethodField()

    class Meta:
        model = Lectures
        #fields = ['id', 'title', 'description', 'price', 'youtube_link', 'main_category', 'sub_category', 'writer', 'enroll_students', 'enroll_cnt', 'like_members', 'like_cnt', 'visit_cnt', 'create_date', 'writer', 'images']
        fields = '__all__'

    #SerializerMethodFiled에 사용할 메소드 정의
    def get_images(self, obj):
        image=obj.lectures_image.all()
        return LectuerImageSerializer(instance=image, 
                                    many=True, 
                                    context=self.context).data

    '''
    장고에서 모델간의 manyTomany관계를 정의할 때 반드시 생성된 객체에
    대해서만 정의 가능하다.
    즉, create메소드를 통해서 테이블에 데이터를 생성하기전에 다른 테이블과
    manyTomany를 지정하는 것은 불가능하다.
    '''
    def create(self, validated_data):
        validated_data.pop('enroll_students',[])
        validated_data.pop('like_members',[])

        instance = Lectures.objects.create(**validated_data)

        image_set = self.context['request'].FILES

        for image_data in image_set.getlist('image'):
            Lecture_Image.objects.create(lecture=instance, image=image_data)
        return instance
    



