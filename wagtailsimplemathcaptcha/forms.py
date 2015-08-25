from wagtail.wagtailforms.forms import FormBuilder
from simplemathcaptcha.fields import MathCaptchaField
from django.utils.translation import ugettext_lazy as _

class MathCaptchaFormBuilder(FormBuilder):
    def __init__(self, fields):
        super(MathCaptchaFormBuilder, self).__init__(fields)
        # Add mathcaptcha to FIELD_TYPES declaration
        self.FIELD_TYPES.update({'mathcaptcha': self.create_mathcaptcha_field})

    def create_mathcaptcha_field(self, field, options):
        return MathCaptchaField(**options)

    @property
    def formfields(self):
        # Add mathcaptcha to formfields property
        fields = super(MathCaptchaFormBuilder, self).formfields
        fields['sweetcaptcha'] = MathCaptchaField(label=_("Prove you're human"))

        return fields