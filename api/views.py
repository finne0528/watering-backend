from django.http import JsonResponse, HttpRequest
from django.views.decorators.http import require_POST
from .constants import ErrorResponse
from .models import WateringSettings

# Create your views here.


@require_POST
def create_watering_setting(request: HttpRequest) -> JsonResponse:
    guild_id: str = request.POST.get('guild_id', None)

    if guild_id is None:
        return JsonResponse(
            status=500,
            data={
                'result': 'failure',
                'error_code': ErrorResponse.REQUIRE_PARAMETER.value,
            }
        )

    WateringSettings(
        guild_id=guild_id,
        interval=None,
    ).save()

    return JsonResponse(
        status=200,
        data={
            'result': 'success'
        }
    )


@require_POST
def update_auto_watering_interval(request: HttpRequest) -> JsonResponse:
    interval: str = request.POST.get('interval', None)
    guild_id: str = request.POST.get('guild_id', None)

    if (interval is None) or (guild_id is None):
        return JsonResponse(
            status=500,
            data={
                'result': 'failure',
                'error_code': ErrorResponse.REQUIRE_PARAMETER.value,
            }
        )

    if not interval.isdigit():
        return JsonResponse(
            status=500,
            data={
                'result': 'failure',
                'error_code': ErrorResponse.INVALID_PARAMETER_FORMAT.value,
            }
        )

    try:
        watering_setting = WateringSettings.objects.get(guild_id=guild_id)
    except:
        return JsonResponse(
            status=404,
            data={
                'result': 'failure',
                'error_code': ErrorResponse.WATERING_SETTING_NOT_FOUND.value
            }
        )

    old_interval: int = watering_setting.interval

    watering_setting.interval = interval
    watering_setting.save()

    return JsonResponse(
        status=200,
        data={
            "result": "success",
            "interval": {
                "old": old_interval,
                "new": interval
            }
        }
    )
