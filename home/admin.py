# 后台管理
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from home.db import get_db
from home.auth import login_required

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/', methods=('GET', 'POST'))
@login_required
def admin():
    return render_template('admin/index.html')
