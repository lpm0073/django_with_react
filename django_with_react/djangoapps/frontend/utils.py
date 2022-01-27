from django.contrib.staticfiles.finders import find
from django.contrib.staticfiles.storage import staticfiles_storage


def static_fallback_open(static_path, mode="r"):
    """
    attempts to open static_path first within collected
    staticfiles storage.

    if that doesn't work then next does a file system search
    for the file and if located then attempts opening using
    standard file i/o.
    """
    writing = "w" in mode or "a" in mode

    if writing or staticfiles_storage.exists(static_path):
        return staticfiles_storage.open(static_path, mode)

    # fall back to finders path
    absolute_path = find(static_path)
    if absolute_path is None:
        raise IOError("{0} does not exist".format(static_path))

    return open(absolute_path, mode)
