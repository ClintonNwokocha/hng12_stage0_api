from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import pytz

def get_info(request):
    current_datetime = datetime.now(pytz.utc).replace(microsecond=0).isoformat()
    current_datetime = current_datetime.split("+")[0] + "Z"
    data = {
            "email": "leoclinton2011@hotmail.com",
            "current_datetime": current_datetime,
            "github_url": "https://github.com/ClintonNwokocha/hng12_stage0_api"
            }
    return JsonResponse(data, json_dumps_params={'indent': 4})
