from crontab import CronTab


def run():
    cron = CronTab(user="hubert322")
    job = cron.new(command="python3 update.py")
    job.minute.every(1)

    cron.write()


if __name__ == '__main__':
    run()
