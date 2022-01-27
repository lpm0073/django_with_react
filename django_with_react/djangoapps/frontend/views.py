import json

from django.contrib.staticfiles.finders import find
from django.contrib.staticfiles.storage import staticfiles_storage
from django.shortcuts import render


def static_fallback_open(static_path, mode="r"):
    writing = "w" in mode or "a" in mode

    if writing or staticfiles_storage.exists(static_path):
        return staticfiles_storage.open(static_path, mode)

    # fall back to finders path
    absolute_path = find(static_path)
    if absolute_path is None:
        raise IOError("{0} does not exist".format(static_path))

    return open(absolute_path, mode)


def index(request):
    """
    Dynamically build the equivalent of react's build/index.html file
    by extracting the reactjs css and js entry points from
    build/asset-manifest.json

    the literal file path is: /app/django_with_react/djangoapps/frontend/build/asset-manifest.json
    the relative path of `reactjs/asset-manifest.json` is due
    to settings/base.py STATICFILES_DIRS

    Background:
    ./build/asset-manifest.json is the top-most result of having run `yarn run build`
    from the root of this Django app `./django_with_react/djangoapps/frontend`. The React build script
    yields a production-ready transpilation of the entire React project.

    The goal of this view is to correctly generate the <head> and <body> elements that
    are generated as build/index.html. The salient elements of this file are derived from
    the contents of the json dictionary build/asset-manifest.json.

    Example asset-manifest.json
        {
        "files": {
            "main.css": "/static/css/main.073c9b0a.css",
            "main.js": "/static/js/main.f8921527.js",
            "static/media/logo.svg": "/static/media/logo.4bdbcf8396881de06a6723a92fed910b.svg",
            "index.html": "/index.html",
            "main.073c9b0a.css.map": "/static/css/main.073c9b0a.css.map",
            "main.f8921527.js.map": "/static/js/main.f8921527.js.map"
        },
        "entrypoints": [
            "static/css/main.073c9b0a.css",
            "static/js/main.f8921527.js"
        ]
        }

    Example output:

        <head>
            <link href="/static/css/main.073c9b0a.css" rel="stylesheet">
            <script defer="defer" src="/static/js/main.f8921527.js"></script>
        </head>
        <body>
            <noscript>You need to enable JavaScript to run this app.</noscript>
            <div id="reactjs-root"></div>
        </body>

    """
    asset_manifest = {}
    with static_fallback_open("reactjs/asset-manifest.json") as json_file:
        asset_manifest = json.load(json_file)

    react_css_bundle = asset_manifest["files"]["main.css"]
    react_js_bundle = asset_manifest["files"]["main.js"]

    context = {"react_css_bundle": react_css_bundle, "react_js_bundle": react_js_bundle}
    return render(request, "index.html", context=context)
