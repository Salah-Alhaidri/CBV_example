from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    titile=models.CharField(max_length=50)
    content=models.TextField(max_length=1000)
    created_at=models.DateField(default=timezone.now)
    img=models.ImageField(upload_to='post-img/',null=True)
    active=models.BooleanField(default=False)
    

    

    # class Meta:
        # verbose_name = _("")
        # verbose_name_plural = _("s")

    def __str__(self):
        return self.titile

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
