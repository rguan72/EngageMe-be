from app.models.intervals import Interval


def average_interval_update():
    interval = Interval({
        "url": "hello",
        "start": 1,
        "end": 2,
        "uuid": "hubert322"
    })
    interval.commit()
    print("HI")


if __name__ == '__main__':
    average_interval_update()
