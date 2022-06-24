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
            redirect('dropbox')
    else:
        form = MainForm()

        ctx = {
            "form": form
        }

    return render(request, 'coralnet/home.html', ctx)

def dropbox_view(request):
    dbx = dropbox.Dropbox(
        oauth2_refresh_token = settings.DBX_REFRESH_TOKEN,
        app_key = settings.DBX_APP_KEY,
        app_secret = settings.DBX_APP_SECRET
    )

    dbx.check_and_refresh_access_token()

    tmp_name = tempfile.TemporaryDirectory().name.split('/')[-1]
    dbx_dir = dbx.file_requests_create(tmp_name, f'/{tmp_name}')

    ctx = {
        "dbx_link": dbx_dir.url
    }

    return render(request, 'coralnet/dropbox.html', ctx)
