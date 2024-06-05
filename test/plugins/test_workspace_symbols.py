# Copyright 2017-2020 Palantir Technologies, Inc.
# Copyright 2021- Python Language Server Contributors.

import os
import sys

import pytest

from pylsp import uris
from pylsp.lsp import SymbolKind
from pylsp.plugins.workspace_symbol import pylsp_workspace_symbol
from pylsp.workspace import Workspace

PY2 = sys.version[0] == "2"
LINUX = sys.platform.startswith("linux")
CI = os.environ.get("CI")
DOC_URI = uris.from_fs_path(__file__)
DOC = """import sys

a = 'hello'

class B:
    def __init__(self):
        x = 2
        self.y = x

def main(x):
    y = 2 * x
    return y

"""


def test_symbols_empty_query(config, workspace):
    config.update({"plugins": {"jedi_workspace_symbols": {"enabled": True}}})
    symbols = pylsp_workspace_symbol(config, workspace, "")

    assert len(symbols) == 0


def test_symbols_nonempty_query(config, workspace):
    config.update({"plugins": {"jedi_workspace_symbols": {"enabled": True}}})
    symbols = pylsp_workspace_symbol(config, workspace, "main")

    assert len(symbols) == 0


#
# def test_symbols_all_scopes(config, workspace):
#     doc = Document(DOC_URI, workspace, DOC)
#     symbols = pylsp_document_symbols(config, doc)
#     helper_check_symbols_all_scope(symbols)
#
#
# def test_symbols_non_existing_file(config, workspace, tmpdir):
#     path = tmpdir.join("foo.py")
#     # Check pre-condition: file must not exist
#     assert not path.check(exists=1)
#
#     doc = Document(uris.from_fs_path(str(path)), workspace, DOC)
#     symbols = pylsp_document_symbols(config, doc)
#     helper_check_symbols_all_scope(symbols)
#
#
# @pytest.mark.skipif(
#     PY2 or not LINUX or not CI, reason="tested on linux and python 3 only"
# )
# def test_symbols_all_scopes_with_jedi_environment(workspace):
#     doc = Document(DOC_URI, workspace, DOC)
#
#     # Update config extra environment
#     env_path = "/tmp/pyenv/bin/python"
#     settings = {"pylsp": {"plugins": {"jedi": {"environment": env_path}}}}
#     doc.update_config(settings)
#     symbols = pylsp_document_symbols(doc._config, doc)
#     helper_check_symbols_all_scope(symbols)
