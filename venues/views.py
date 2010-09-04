from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from avatar.templatetags.avatar_tags import avatar


if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification
else:
    notification = None



def index(request, template_name="venues/index.html", extra_context=None):
    return render_to_response(template_name, {}, context_instance=RequestContext(request))
