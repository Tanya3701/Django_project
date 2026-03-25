from django.forms.models import ModelForm
from django.core.exceptions import ValidationError

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        error_messages = {}


    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        name = cleaned_data.get("product_name")
        description = cleaned_data.get("description")

        blocked_words_list = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

        if name and description:
            for word in blocked_words_list:
                if word.lower() in name.lower() or word.lower() in description.lower():
                    raise ValidationError(f'В наименовании или описании товара использовано недопустимое выражение "{word}"')




