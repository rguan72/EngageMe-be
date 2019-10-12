from app.models.intervals import Interval
from datetime import datetime


def average_interval_update():
    now = datetime.now()
    interval = Interval({
        "url": "hello",
        "start": 1,
        "end": 2,
        "uuid": now.strftime("%d/%m/%Y %H:%M:%S")
    })
    interval.commit()


average_interval_update()
