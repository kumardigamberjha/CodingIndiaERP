from django.forms import ModelForm

from UserReq.models import Requisition

class ReqForm(ModelForm):
    class Meta:
        model = Requisition
        fields = "__all__"