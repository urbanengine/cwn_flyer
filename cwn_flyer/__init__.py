#! /usr/bin/env python3

import os
import logging


from flask import Flask
from webassets.loaders import PythonLoader as PythonAssetsLoader

from cwn_flyer.controllers.main import main
from cwn_flyer import assets

from cwn_flyer.extensions import (
        cache,
        assets_env,
        debug_toolbar,
    )

def create_app(object_name, env="prod"):
    app = Flask(__name__)
    app.config.from_object(object_name)
    app.config['ENV'] = env

    cache.init_app(app)
    debug_toolbar.init_app(app)
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)
    app.register_blueprint(main)
    return app