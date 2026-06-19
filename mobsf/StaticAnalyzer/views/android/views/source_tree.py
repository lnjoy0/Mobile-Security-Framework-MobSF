# -*- coding: utf_8 -*-
"""List all java files."""

import logging
from pathlib import Path

from django.conf import settings
from django.shortcuts import (
    loader,
    render,
)

from mobsf.MobSF.utils import (
    is_md5,
    print_n_send_error_response,
)
from mobsf.StaticAnalyzer.views.common.shared_func import (
    find_java_source_folder,
)
from mobsf.MobSF.views.authentication import (
    login_required,
)

logger = logging.getLogger(__name__)


# Generator that uses 2 template files in order to make the main template
def tree_index_maker(root_dir: Path, original_root_dir_len: int):
    def _index(root, root_len):
        for mfile in root.iterdir():
            if mfile.is_dir():
                yield loader.render_to_string(
                    'static_analysis/treeview_folder.html',
                    {'file': mfile.name,
                     'subfiles': _index(mfile, root_len)},
                )
                continue
            yield loader.render_to_string(
                'static_analysis/treeview_file.html',
                {'file': mfile.name,
                 'path': mfile.as_posix()[root_len + 1: -len(mfile.name)]},
            )
    return _index(root_dir, original_root_dir_len)


