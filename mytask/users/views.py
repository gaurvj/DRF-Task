from django.http import HttpResponse
from users.models import UserInfo, ActivityPeriod
import json


#To get all the activity log of users.
def UserActivtiyDetails(request):
    try:
        members = []
        for i in UserInfo.objects.all():
            activity = []
            for j in ActivityPeriod.objects.filter(user_id=i.id):
                activity.append({
                    "start_time": j.start_time,
                    "end_time": j.end_time
                })
            members.append({
                "id": i.id,
                "real_name": i.real_name,
                "tz": i.tz,
                "activity_periods": activity
            })

        result = {"ok": True,
                  "members": members}
        return HttpResponse(json.dumps(result))
    except Exception as e:
        print(e)