from django.db import models


'''
class KallistoAttributes(models.Model):
    attribute = models.CharField(max_length=32)

    def __unicode__(self):
        return self.attribute

    def __str__(self):
        return self.attribute


class KallistoEntryIDs(models.Model):
    entry_id = models.CharField(max_length=128)
    attributes = models.ManyToManyField(KallistoAttributes, through='KallistoData')

    def __unicode__(self):
        return self.entry_id

    def __str__(self):
        return self.entry_id


class KallistoData(models.Model):
    entry_id = models.ForeignKey(KallistoEntryIDs, on_delete=models.CASCADE)
    attribute = models.ForeignKey(KallistoAttributes, on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)


class RsemAttributes(models.Model):
    attribute = models.CharField(max_length=32)

    def __unicode__(self):
        return self.attribute

    def __str__(self):
        return self.attribute


class RsemEntryIDs(models.Model):
    entry_id = models.CharField(max_length=128)
    attributes = models.ManyToManyField(RsemAttributes, through='RsemData')

    def __unicode__(self):
        return self.entry_id

    def __str__(self):
        return self.entry_id


class RsemData(models.Model):
    entry_id = models.ForeignKey(RsemEntryIDs, on_delete=models.CASCADE)
    attribute = models.ForeignKey(RsemAttributes, on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)


class SailfishAttributes(models.Model):
    attribute = models.CharField(max_length=32)

    def __unicode__(self):
        return self.attribute

    def __str__(self):
        return self.attribute


class SailfishEntryIDs(models.Model):
    entry_id = models.CharField(max_length=128)
    attributes = models.ManyToManyField(SailfishAttributes, through='SailfishData')

    def __unicode__(self):
        return self.entry_id

    def __str__(self):
        return self.entry_id


class SailfishData(models.Model):
    entry_id = models.ForeignKey(SailfishEntryIDs, on_delete=models.CASCADE)
    attribute = models.ForeignKey(SailfishAttributes, on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)
'''
