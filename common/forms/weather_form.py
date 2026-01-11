from django import forms


class WeatherForm(forms.Form):
    city = forms.CharField(required=True)
    output_format = forms.CharField(required=True)

    def clean_output_format(self):
        output_format = self.cleaned_data["output_format"].lower()

        if output_format not in ["json", "xml"]:
            raise forms.ValidationError(
                "output_format must be either 'json' or 'xml'"
            )

        return output_format
