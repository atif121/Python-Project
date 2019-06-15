from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    slug=models.SlugField(max_length=150,unique=True,db_index=True)
    store_logo=models.ImageField(upload_to='static/%y/%m/%d',blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering =('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):
        return self.name     

    def get_absolute_url(self):
        return reverse('store:book_list_by_category',args=[self.slug])


class Book(models.Model):
    category=models.ForeignKey(Category,related_name='books',on_delete=models.CASCADE)
    name=models.CharField(max_length=100,db_index=True)
    slug=models.SlugField(max_length=150,db_index=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(blank=True)
    stock=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='books/%y/%m/%d',blank=True)
    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:book_detail',args=[self.id,self.slug])