from django.db import models
from django.contrib.postgres.fields import ArrayField



class SortedData (models.Model):
    kind = models.CharField(max_length=15,db_index=True, verbose_name='Kind of sorting')
    beforesort = ArrayField(base_field=models.IntegerField(verbose_name='Start list'))
    aftersort = ArrayField(base_field=models.IntegerField(verbose_name='Finish list'))
    exectime = models.IntegerField(verbose_name='Time of execution')
    timestart = models.DateTimeField(verbose_name='Start of execution', db_index=True, null=True)

    class Meta:
        verbose_name_plural ='Records of sorted data'
        verbose_name ='Record of sorted data'
        ordering =['-timestart']
