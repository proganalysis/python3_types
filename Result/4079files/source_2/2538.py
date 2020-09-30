from app import db
from sqlalchemy import Integer, Date, Time, Column, ForeignKey, exc
import datetime


class Item(db.Model):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    reservations = db.relationship('Reservation')

    # add your own columns/relationships here
    # ----

    def __getstate__(self):
        return {'id': self.id, 'reservations': [r.__getstate__() for r in self.reservations]}


class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    date = Column(Date, index=True, nullable=False)
    start_time = Column(Time, nullable=False)
    duration = Column(Integer, nullable=False)
    # add your own columns/relationships here
    # ----

    def __getstate__(self):
        """
        start_time format is hh:mm:ss
        duration in minutes
        :return: tuple
        """
        return {
                'id': self.id, 'item_id': self.item_id, 'date': self.date.isoformat(),
                'start_time': self.start_time.strftime('%X'), 'duration': self.duration
                }

    def update_from_json(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
        if not isinstance(self.date, datetime.date):
            self.date = datetime.datetime.strptime(self.date, '%Y-%m-%d').date()
        if not isinstance(self.start_time, datetime.time):
            self.start_time = datetime.datetime.strptime(self.start_time, '%X').time()

# also you can add more models and relationships to build more complex business logic
# ----
