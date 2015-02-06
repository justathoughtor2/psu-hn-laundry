from django.db import models

class Query(models.Model):
    query_text = models.CharField(max_length=200)
    def __unicode__(self):
        return u'%s' % (self.query_text)

class Response(models.Model):
    query = models.ForeignKey(Query)
    machine_type = models.CharField(max_length=200)
    machine_in_use = models.IntegerField(default=-1)
    def __unicode__(self):
        return u'%s' % (self.response_text)
