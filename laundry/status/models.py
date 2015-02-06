from django.db import models

class Query(models.Model):
    query_text = models.CharField(max_length=200)
    def __unicode__(self):
        return u'%s' % (self.query_text)

class Response(models.Model):
    query = models.ForeignKey(Query)
    response_type = models.CharField(max_length=200)
    in_use = models.BooleanField(default=False)
    def __unicode__(self):
        return u'%s' % (self.response_text)
