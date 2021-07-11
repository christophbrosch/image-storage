import django_tables2 as tables
from .models import ImageTransaction, AnnotationTransaction

class ImageTransactionTable(tables.Table):
    actions = tables.TemplateColumn(
        template_code="""
                        <div class="d-flex justify-content-around">
                            <a class="btn btn-danger" href="{% url \'datasets:image-transactions-delete\' record.dataset.id record.id %}"> Löschen </a>
                        </div>
                        """,
        orderable = False
    )
    class Meta:
        model = ImageTransaction
        template_name = 'django_tables2/bootstrap.html'
        fields = ['id', 'created_at', 'actions']

class AnnotationTransactionTable(tables.Table):
    actions = tables.TemplateColumn(
        template_code="""
                        <div class="d-flex justify-content-around">
                            <a class="btn btn-danger" href="{% url \'datasets:annotation-transactions-delete\' record.dataset.id record.id %}"> Löschen </a>
                        </div>
                        """,
        orderable = False
    )
    class Meta:
        model = AnnotationTransaction
        template_name = 'django_tables2/bootstrap.html'
        fields = ['id', 'created_at', 'actions']