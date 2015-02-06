from django.db import models

class Query(models.Model):
    query_text = models.CharField(max_length=200)

class Response(models.Model):
    query = models.ForeignKey(Query)
    response_text = models.CharField(max_length=200)
    available = models.IntegerField(default=10)
