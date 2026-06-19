# -*- coding: utf_8 -*-
"""View Source of a file."""
import logging
import ntpath
from pathlib import Path

from django.conf import settings
from django.shortcuts import render
from django.utils.html import escape
from django.http import JsonResponse

from mobsf.MobSF.forms import FormUtil
from mobsf.MobSF.utils import (
    is_safe_path,
    print_n_send_error_response,
)
from mobsf.StaticAnalyzer.views.common.shared_func import (
    find_java_source_folder,
)
from mobsf.StaticAnalyzer.forms import (
    ViewSourceAndroidApiForm,
    ViewSourceAndroidForm,
)
from mobsf.MobSF.views.authentication import (
    login_required,
)

logger = logging.getLogger(__name__)


