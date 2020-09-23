import sqlalchemy
from flask import render_template, request, flash, redirect, url_for, session

from app.blueprints.test import bp

from app.database import db_session

from app.models import Test as Model
from app.tables import TestTable as Table
from app.forms import TestForm as Form


title = bp.name


@bp.route("/")
def view_all():
    elements = Model.query.all()
    table = Table(elements)

    return render_template("table_view.html", title=title, table=table)


@bp.route("/create", methods=["GET", "POST"])
def create_model():
    form = Form(request.form)
    del form.delete

    if request.method == 'POST' and form.validate():
        new_el = Model()
        for field in form:
            if field.type == "SubmitField":
                continue

            if field.data == "":
                continue

            setattr(new_el, field.name.lower(), field.data)

        db_session.add(new_el)
        try:
            db_session.commit()
        except (sqlalchemy.exc.IntegrityError, sqlalchemy.orm.exc.FlushError) as e:
            flash(str(e), "danger")

        return redirect(url_for(".view_all"))

    return render_template("form_view.html", title=title, form=form)


@bp.route("/edit", methods=["GET", "POST"])
def edit_model():
    model_id = request.args.get("id")
    model = Model.query.filter_by(id=model_id).first()

    form = Form(**model.__dict__)

    if request.method == 'POST' and form.validate():
        form = Form(request.form)

        if form.delete.data == True:
            db_session.delete(model)
            db_session.commit()

            flash("Model deleted", "primary")

            return redirect(url_for(".view_all"))

        for field in form:
            if field.type == "SubmitField":
                continue

            if field.data == "":
                continue

            setattr(model, field.name.lower(), field.data)

        try:
            db_session.commit()
            flash("Model updated", "primary")
        except (sqlalchemy.exc.IntegrityError, sqlalchemy.orm.exc.FlushError) as e:
            flash(str(e), "danger")

        return redirect(url_for(".view_all"))

    return render_template("form_view.html", title=title, form=form)
