import math

from django.shortcuts import render

from ...models import ImageTransaction, AnnotationTransaction
from ...tables import ImageTransactionTable, AnnotationTransactionTable

def image_table_pagination(request, pk, page):
    """ Renders the transaction table based off given dataset id and page number """
    table_class = ImageTransactionTable
    table_data = ImageTransaction.objects.filter(dataset__id=pk)[(page - 1) * 3: (page - 1) * 3 + 3] # -1 becuase list indices start with 0 instead of 1
    table = table_class(table_data)
    return render(request, 'transactions/htmx/image-table.html', context={'pk': pk, 
                                                                    'table': table, 
                                                                    'pages': range(1, max(1, int(math.ceil(len(ImageTransaction.objects.all()) / 3))) + 1),
                                                                    'current_page': page})

def annotation_table_pagination(request, pk, page):
    """ Renders the transaction table based off given dataset id and page number """
    table_class = AnnotationTransactionTable
    table_data = AnnotationTransaction.objects.filter(dataset__id=pk)[(page - 1) * 3: (page - 1) * 3 + 3] # -1 becuase list indices start with 0 instead of 1
    table = table_class(table_data)
    return render(request, 'transactions/htmx/annotation-table.html', context={'pk': pk, 
                                                                    'table': table, 
                                                                    'pages': range(1, max(1, int(math.ceil(len(AnnotationTransaction.objects.all()) / 3))) + 1),
                                                                    'current_page': page})                                                                    