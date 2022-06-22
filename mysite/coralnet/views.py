from django.shortcuts import render
from django.conf import settings
import dropbox
import tempfile

# Create your views here.
def home(request):
    if request.method == 'POST':
        redirect('success')
    else:
        dbx = dropbox.Dropbox(settings.DBX_ACCESS_TOKEN)
        tmp_name = tempfile.TemporaryDirectory().name.split('/')[-1]
        dbx_dir = dbx.file_requests_create(tmp_name, f'/{tmp_name}')

        ctx = {
            "dbx_link": dbx_dir.url
        }

    return render(request, 'coralnet/home.html', ctx)

def success(request):
    render(request, 'coralnet/succes.html', {})
