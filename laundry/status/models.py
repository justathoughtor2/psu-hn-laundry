from django.db import models

class Query(models.Model):
    query_text = models.CharField(max_length=200)
    def __unicode__(self):
        return u'%s' % (self.query_text)

class Response(models.Model):
    query = models.ForeignKey(Query)
    machine_type = models.CharField(max_length=200)
    in_use = models.BooleanField(default=False)
    num_machines = models.IntegerField(default=10)
    def __unicode__(self):
        return u'%s' % (self.response_text)
