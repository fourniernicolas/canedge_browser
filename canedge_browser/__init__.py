from canedge_browser.listing import get_log_files
from canedge_browser.support.LocalFileSystem import LocalFileSystem
import canedge_browser.config as config

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
