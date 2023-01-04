from django.db import models
from datetime import datetime

"""list for like or dislike choice"""
LIKE_CHOICES = (
    ("like", "like"),
    ("like", "like"),
    
)

# Create your models here.
"""user table model"""
class Usermodel(models.Model):

    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    created_at = models.TimeField(default= datetime.utcnow)


"""post table model"""
class Postmodel(models.Model):

    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=datetime.utcnow)
    post_id = models.IntegerField(primary_key= True)
    user_id = models.ForeignKey(Usermodel, on_delete = models.CASCADE, related_name = "post")


    def __str__(self):

        return self.text    
    
        
"""like table model"""
class Likemodel(models.Model):

    resp_id = models.IntegerField(primary_key= True)
    post_id = models.ForeignKey(Postmodel, on_delete = models.CASCADE, related_name = "like" )
    user_id = models.ForeignKey(Usermodel, on_delete=models.CASCADE , related_name='like')
    like = models.CharField(max_length=10, choices = LIKE_CHOICES, default= "like")
    created_at = models.DateTimeField(default= datetime.utcnow)
    updated_at = models.DateTimeField(default= datetime.utcnow)

    def __str__(self):

        return self.user_id

    def __repr__(self):
        
        return  f'{self.user_id}'



    