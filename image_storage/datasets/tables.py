import django_tables2 as tables
from .models import ImageTransaction

class ImageTransactionTable(tables.Table):
    actions = tables.TemplateColumn(
        template_code="""
                        <div class="d-flex justify-content-around">
                            <a class="btn btn-danger" href="{% url \'datasets:transactions-delete\' record.id %}"> Löschen </a>
                        </div>
                        """,
        orderable = False
    )
    class Meta:
        model = ImageTransaction
        template_name = 'django_tables2/bootstrap.html'
        fields = ['id', 'created_at', 'actions']