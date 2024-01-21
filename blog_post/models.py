from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Catagory(models.Model):
    name=models.CharField( max_length=50)
    slug= models.SlugField(null=True,blank=True ,unique=True)

    def __str__(self) -> str:
        return self.name
    




class Profile(models.Model):
    name=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField()
    join_data=models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name.username

class Post(models.Model):
    title=models.CharField( max_length=70)
    des= models.TextField()
    date_time=models.DateTimeField( auto_now_add=True)
    catagory=models.ManyToManyField(Catagory)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    img=models.ImageField( upload_to='media',null=True,blank=True )

    def __str__(self) -> str:
        return self.title
    



class Comments(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    comment=models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.user.username