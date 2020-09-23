#!/usr/bin/env wpython
#-*- coding: utf-8 -*-

import dotenv
import os


dotenv.load_dotenv()


def create_app():
    from app import app
    from app.database import init_db

    init_db()

    app.debug = int(os.getenv("IS_FLASK_DEBUG"))
    app.secret_key = os.getenv("FLASK_SECRET")

    return app


if __name__ == '__main__':
    create_app().run(port=1234)
