import math
import traceback

from django.urls import reverse, reverse_lazy
from django.db.models.query import QuerySet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, FormView, ListView, DetailView, CreateView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
from django.shortcuts import render

from django_tables2.views import SingleTableMixin

from ..models import Dataset, Image, Annotation, ImageTransaction, AnnotationTransaction
from ..forms import ImageUploadForm, AnnotationUploadForm
from ..tables import ImageTransactionTable

class ListView(LoginRequiredMixin, ListView):
    model = Dataset
    template_name = 'datasets/list.html'
    context_object_name = 'datasets'

    def get_queryset(self) -> QuerySet[Dataset]:
        """Only return datasets where user is owneer"""
        # queryset = super().get_queryset()
        # return queryset.filter(owner=self.request.user)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        """Turn query into JSON"""
        context = super().get_context_data(**kwargs)
        context['datasets'] = [dataset for dataset in context['datasets'].values()]

        # Add url for every detailview for easy access on frontend
        for dataset in context['datasets']:
            dataset['detail_url'] = reverse('datasets:detail', kwargs={'pk': dataset['id']})
            dataset['delete_url'] = reverse('datasets:delete', kwargs={'pk': dataset['id']})

        return context

class DatasetDetailView(LoginRequiredMixin, SingleTableMixin, DetailView):
    template_name = 'datasets/detail.html'
    model = Dataset
    table_class = ImageTransactionTable

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_upload_form'] = ImageUploadForm()
        context['annotation_upload_form'] = AnnotationUploadForm()
        context['images'] = Image.objects.filter(dataset__id=self.kwargs['pk'])[:6]
        context['pages'] = range(1, max(1, int(math.ceil(len(ImageTransaction.objects.all()) / 3))) + 1)
        context['current_page'] = 1
        return context
    
    def get_table_data(self):
        return ImageTransaction.objects.filter(dataset__id=self.kwargs['pk'])[:3]

class ImageUploadFormView(LoginRequiredMixin, SingleObjectMixin, FormView):
    template_name = 'datasets/detail.html'
    form_class = ImageUploadForm
    model = Dataset

    def post(self, request, pk, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            try:
                dataset = Dataset.objects.get(pk = pk)
            except Dataset.DoesNotExist:
                messages.add_message('Kritischer Fehler')
            else:
                try:
                    transaction = ImageTransaction.objects.create(dataset = dataset)
                except:
                    messages.add_message('Kritischer Fehler')
                else:
                    for file in files:
                        try:
                            image = Image.objects.create(file = file, dataset = dataset)
                        except Exception as e:
                            # TODO: Logging
                            messages.add_message(request, messages.WARNING, file.name + ' fehler beim upload aufgetreten.')
                        else:
                            transaction.images.add(image)
                            messages.add_message(request, messages.INFO, file.name + ' erfolgreich hochgeladen.')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self) -> str:
        return reverse('datasets:detail', kwargs={'pk': self.object.pk})

class AnnotationUploadFormView(LoginRequiredMixin, SingleObjectMixin, FormView):
    template_name = 'datasets/detail.html'
    form_class = AnnotationUploadForm
    model = Dataset

    def post(self, request, pk, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')

        if form.is_valid():
            dataset = Dataset.objects.get(pk = pk)
            
            # TODO: Check if file ending corresponds to what the dataset.annotation_file_format requires
            mapping = {'pascal_voc': 'xml', 'yolo': 'txt', 'coco': 'json'} # Everything beside pascal_voc is a lie
            expected_file_extension = mapping[dataset.annotation_file_format]
            try:
                transaction = AnnotationTransaction.objects.create(dataset=dataset)
            except:
                traceback.print_exc()
            else:
                for file in files:
                    if file.name.split('.')[-1] != expected_file_extension:
                        continue
                    else:
                        print(''.join(file.name.split('.')[0:-1]))
                        try:
                            image = Image.objects.get(name=''.join(file.name.split('.')[0:-1]))
                        except Image.DoesNotExist:
                            traceback.print_exc()
                            messages.add_message(request, messages.WARNING, file.name + ' fehler beim upload aufgetreten.')
                        else:
                            try:
                                annotation = Annotation.objects.create(file = file, image = image, format = 'pascal_voc')
                            except:
                                traceback.print_exc()
                                messages.add_message(request, messages.WARNING, file.name + ' fehler beim upload aufgetreten.')  
                            else:
                                transaction.annotations.add(annotation)
                                messages.add_message(request, messages.INFO, file.name + ' erfolgreich hochgeladen.')


            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def get_success_url(self) -> str:
        return reverse('datasets:detail', kwargs={'pk': self.object.pk})

class DetailView(View):
    
    def get(self, request, *args, **kwargs):
        view = DatasetDetailView.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        if request.POST['form'] == 'image_upload_form':
            view = ImageUploadFormView.as_view()
        elif request.POST['form'] == 'annotation_upload_form':
            view = AnnotationUploadFormView.as_view()
        return view(request, *args, **kwargs)

# Create your views here.
class CreateView(LoginRequiredMixin, CreateView):
    model = Dataset
    fields = ['name', 'description', 'annotation_file_format', 'labels']
    template_name = 'datasets/create.html'

    def get_success_url(self) -> str:
        """Add owner to newly created dataset object"""
        object = self.object
        object.owner = self.request.user
        object.save()
        return reverse('dashboard:index') 

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Dataset
    template_name = 'datasets/delete.html'
    success_url = reverse_lazy('dashboard:index')
