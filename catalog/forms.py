from django.core.exceptions import ValidationError
from django.forms.models import ModelForm

from catalog.models import Product

BLOCKED_WORD_LIST = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["product_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите наименование товара"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Добавьте описание товара"}
        )
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Задайте стоимость товара"}
        )
        self.fields["inventory"].widget.attrs.update(
            {"class": "form-check", "type": "checkbox"}
        )

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        name = cleaned_data.get("product_name")
        description = cleaned_data.get("description")

        if name and description:
            for word in BLOCKED_WORD_LIST:
                if word.lower() in name.lower() or word.lower() in description.lower():
                    raise ValidationError(
                        f'В наименовании или описании товара использовано недопустимое выражение "{word}"'
                    )

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 100:
            raise ValidationError("Стоимость не может быть отрицательной")
        return price
