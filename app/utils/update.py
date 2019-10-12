from apscheduler.schedulers.background import BackgroundScheduler


def average_interval_update():
    print("HI")


def run():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=average_interval_update(), trigger="interval", seconds=3)
    scheduler.start()
