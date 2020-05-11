from app import application, db
from app.utils.representation import DictOrDateTime
from flask import Response, request, json
from app.models import Item, Reservation
from sqlalchemy import exc


# boilerplate
response = Response(content_type='application/json; charset=utf-8')


@application.route("/", methods=['GET'])
@application.route("/fetch", methods=['GET'])
def get_all():
    items = Item.query.all() or []
    response.response = json.dumps(items, cls=DictOrDateTime)
    return response


@application.route("/fetch/<int:id>", methods=['GET'])
def get_by_id(id):
    item = Item.query.filter_by(id=id).first()
    response.response = json.dumps(item, cls=DictOrDateTime)
    return response


@application.route("/create", methods=['POST'])
def create():
    item = json.loads(request.form['item'])
    reservation = Reservation()
    reservation.update_from_json(**item)
    try:
        db.session.add(reservation)
        db.session.commit()
    except exc.OperationalError as err:
        response.status_code = 400
        response.response = json.dumps({"message": str(err)})
    except Exception as err:
        response.status_code = 500
        response.response = json.dumps({"message": str(err)})
    else:
        response.status_code = 201
        response.response = json.dumps(item)
    finally:
        return response


@application.route("/update", methods=['PUT', 'PATCH'])
def update():
    item = json.loads(request.form['item'])
    reservation = Reservation.query.filter_by(id=item['id']).first()
    reservation.update_from_json(**item)
    try:
        db.session.add(reservation)
        db.session.commit()
    except exc.OperationalError as err:
        response.status_code = 400
        response.response = json.dumps({"message": str(err)})
    else:
        response.status_code = 204
    finally:
        return response


@application.route("/delete", methods=['DELETE'])
def delete():
    id = request.form['id']
    reservation = Reservation.query.filter_by(id=id).first()
    try:
        db.session.delete(reservation)
        db.session.commit()
    except exc.OperationalError as err:
        response.status_code = 400
        response.response = json.dumps({"message": str(err)})
    else:
        response.status_code = 204
    finally:
        return response
