from rest_framework import serializers
from .models import Usermodel, Postmodel, Likemodel


"""user serializer"""
class Userserializer(serializers.ModelSerializer):

    post = serializers.SlugRelatedField(many=True, read_only= True, slug_field="text")
    
    class Meta:

        model = Usermodel
        fields = ["id", "username", "post"]
        

    """create function create to post data"""
    def create(self, validation_data):

        return Usermodel.objects.create(**validation_data)


    """create function update to put data"""
    def update(self, instance, validated_data):

        instance.id = validated_data.get("id", instance.id)
        instance.username = validated_data.get("username", instance.username)

        instance.save()

        return instance


"""post serializer"""
class Postserializer(serializers.ModelSerializer):

    like_count = serializers.SerializerMethodField() #by serializer method field we can use like_count function and add that data in like_count firld.
    post_by = serializers.CharField(source = 'user_id.username')
  
    class Meta:

        model = Postmodel
        fields = ["post_id", "text", "post_by", "user_id", "like_count","liked_by"]


    """like count function"""
    def get_like_count(self,id):  #this function will count like on a post with the help of post_id.
        
        postid = id
        like_count = Likemodel.objects.filter(post_id = postid ).count()

        return like_count


    """function for display object how like the post"""
    def get_userobj(self,id):

        userid = id
        userobj = Postmodel.objects.filter(user_id = userid).first
        return userobj


    """create function create to post data"""
    def create(self, validation_data):

        return Postmodel.objects.create(**validation_data)


    """create function update to put data"""
    def update(self, instance, validation_data):

        instance.text = validation_data.get("text", instance.text)
        instance.post_id = validation_data.get("post_id", instance.post_id)
        instance.user_id = validation_data.get("user_id", instance.user_id)

        instance.save()

        return instance


"""like serializer"""
class Likeserializer(serializers.ModelSerializer):


  
    class Meta:
  
        model = Likemodel
        fields = ["resp_id","post_id","user_id","like" ]


    """create function create to post data"""
    def create(self, validation_data):

        return Likemodel.objects.create(**validation_data)


    """create function update to put data"""
    def update(self, instance, validation_data):

        instance.resp_id = validation_data.get("resp_id", instance.resp_id)
        instance.post_id = validation_data.get("post_id", instance.post_id)
        instance.user_id = validation_data.get("user_id", instance.user_id)
        instance.like = validation_data.get("like", instance.like)

        instance.save()

        return instance
