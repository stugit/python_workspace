from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views import generic
from django.urls import reverse_lazy
from .models import G1File
from .models import G1FileField
from .models import G1PostingType
from .models import G1FileUploadErrorMessage
from .forms import G1ParseGCIForm


def parse_gci(request):
    file_fields = ()
    split_fields = ()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = G1ParseGCIForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data

            gci_string = form.cleaned_data['gci_string']
            file_name= str(form.cleaned_data['file_name'])

            print("GCI String is: " + gci_string)
            print("file name: " + file_name)
            file_fields = G1FileField.objects.filter(filename__filename=file_name, ftype='DETAIL')
            split_fields = gci_string.split('|')
            i = 0
            for f in file_fields:
                if i < len(split_fields):
                    f.value = split_fields[i]
                i = i + 1

    # if a GET (or any other method) we'll create a blank form
    else:
        form = G1ParseGCIForm(initial={'file_type': G1File.pk})

    return render(request, 'g1_helper/parse_gci_form.html', {'form': form, 'file_fields': file_fields}, {'split_fields': split_fields})


class G1FileView(generic.ListView):
    model = G1File
    template_name = 'g1_helper/g1file.html'
    context_object_name = 'g1_file_list'

    def get_queryset(self):
        return G1File.objects.all()


class G1PostingTypesView(generic.ListView):
    model = G1PostingType
    template_name = 'g1_helper/posting_types.html'
    context_object_name = 'g1_posting_type_list'

    def get_queryset(self):
        return G1PostingType.objects.all()


class G1TradeUploadErrorMessagesView(generic.ListView):
    model = G1FileUploadErrorMessage
    template_name = 'g1_helper/file_upload_error_messages.html'
    context_object_name = 'g1_file_upload_error_message_list'

    def get_queryset(self):
        return G1FileUploadErrorMessage.objects.filter(filename__filename="TRADE_UPLOAD")


class G1SettlementUploadErrorMessagesView(generic.ListView):
    model = G1FileUploadErrorMessage
    template_name = 'g1_helper/file_upload_error_messages.html'
    context_object_name = 'g1_file_upload_error_message_list'

    def get_queryset(self):
        return G1FileUploadErrorMessage.objects.filter(filename__filename="SETTLEMENT_UPLOAD")


class G1FileCreate(CreateView):
    model = G1File
    fields = ['filename']


class G1FileUpdate(UpdateView):
    model = G1File
    fields = ['filename']


class G1FileDelete(DeleteView):
    model = G1File
    success_url = reverse_lazy('g1_file_list')
