from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView

from common.forms.weather_form import WeatherForm
from common.helper_classes.weather_helper import WeatherHelper


class GetCurrentWeather(APIView):
    def post(self, request):
        form = WeatherForm(request.data)

        if not form.is_valid():
            raise Exception(form.errors)

        city = form.cleaned_data["city"]
        output_format = form.cleaned_data["output_format"]

        data = WeatherHelper.fetch_weather(city)
        weather_data = WeatherHelper.extract_weather_data(data)

        if output_format == "json":
            response = WeatherHelper.build_json_response(weather_data)
            return JsonResponse(response)

        xml_response = WeatherHelper.build_xml_response(weather_data)
        return HttpResponse(xml_response, content_type="application/xml")
