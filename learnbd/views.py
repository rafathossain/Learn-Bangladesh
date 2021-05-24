from django.shortcuts import render
from django.http import JsonResponse
import wikipediaapi
from .models import *


# Create your views here.
def index(request):
    # wiki_wiki = wikipediaapi.Wikipedia('en')
    # district = ["bandarban", "rangamati", "khagrachari", "coxs_bazar", "chittagong", "feni", "noakhali", "laxmipur",
    #             "bhola", "rajshahi", "nilphamari", "patuakhali", "barguna", "barisal", "jhalokati", "perojpur",
    #             "chandpur", "comilla", "munshiganj", "brahmanbaria", "narayanganj", "narshingdi", "moulovibazar",
    #             "habiganj", "sylhet", "sunamganj", "netrokona", "kishoreganj", "mymenshingh", "sherpur", "gazipur",
    #             "shariatpur", "madaripur", "dhaka", "manikganj", "tangail", "jamalpur", "bagerhat", "gopalganj",
    #             "faridpur", "khulna", "satkhira", "narail", "jessore", "magura", "jhenaidah", "chuadanga", "meherpur",
    #             "rajbari", "kushtia", "pabna", "sirajganj", "natore", "bogra", "nawabganj", "naogaon", "joypurhat",
    #             "gaibandha", "kurigram", "rangpur", "dinajpur", "lalmonirhat", "thakurgaon", "panchagarh"]
    # for dist in district:
    #     page_py = wiki_wiki.page(str(dist).title())
    #     dist_instance, created_on = DistrictSummary.objects.get_or_create(
    #         dist_id=dist
    #     )
    #     dist_instance.dist_summary = str(page_py.summary)
    #     dist_instance.save()
    return render(request, 'learnbd/index.html')


def getData(request):
    response = []
    if request.method == 'POST':
        summary = DistrictSummary.objects.get(dist_id=request.POST['district'])
        response = [{
            'summary': summary.dist_summary
        }]
    return JsonResponse(response, safe=False)
