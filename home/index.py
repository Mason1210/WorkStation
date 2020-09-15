import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from home.db import get_db

bp = Blueprint('index', __name__)

@bp.route('/', methods=('GET', ))
def index():
    return render_template('index/index.html')