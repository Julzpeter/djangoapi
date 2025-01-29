from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_info(request):
    if request.method == 'GET':
        data = {
            "email":"chepngetichjuliet@gmail.com",
            "current_datetime": datetime.utcnow().isoformat()+ "Z",
            "github_url": "https://github.com/Julzpeter/djangoapi",
        }
        return JsonResponse(data, status=200)
    else:
        return JsonResponse({"error":"Method not allowed"}, status=405)
        

