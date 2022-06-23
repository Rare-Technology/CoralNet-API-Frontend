from django.shortcuts import render
from django.conf import settings
from .forms import MainForm
import dropbox
import tempfile

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = MainForm(request.POST)

        if form.is_valid():
            redirect('success')
    else:
        dbx = dropbox.Dropbox(settings.DBX_ACCESS_TOKEN)
        tmp_name = tempfile.TemporaryDirectory().name.split('/')[-1]
        dbx_dir = dbx.file_requests_create(tmp_name, f'/{tmp_name}')

        form = MainForm()

        ctx = {
            "dbx_link": dbx_dir.url,
            "form": form
        }

    return render(request, 'coralnet/home.html', ctx)

def success(request):
    return render(request, 'coralnet/success.html', {})
