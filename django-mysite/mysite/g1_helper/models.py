from django.urls import reverse
from django.db import models


class G1File(models.Model):
    filename = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('g1file-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.filename


class G1FileField(models.Model):
    filename = models.ForeignKey(G1File, on_delete=models.CASCADE)
    ftype = models.CharField(max_length=20)
    index = models.IntegerField()
    desc = models.CharField(max_length=50)
    vdf = models.CharField(max_length=5, blank=True)
    struct = models.CharField(max_length=15)
    pos = models.CharField(max_length=15)
    comments = models.CharField(max_length=300, blank=True)
    value = ""
 

class G1PostingType(models.Model):
    BL = (
        ('B', 'B'),
        ('L', 'L'),
    )

    posting_type = models.CharField(max_length=3, primary_key=True)
    bl = models.CharField(max_length=1, choices=BL)
    description = models.CharField(max_length=100)


class G1FileUploadErrorMessage(models.Model):
    filename = models.ForeignKey(G1File, on_delete=models.CASCADE)
    code = models.CharField(max_length=2, primary_key=True)
    posted = models.CharField(max_length=1, blank = True)
    description = models.CharField(max_length=150, blank=True)
