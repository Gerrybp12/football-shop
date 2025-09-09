from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi' : 'alobs',
        'name': 'Gerry Bima Putra',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)