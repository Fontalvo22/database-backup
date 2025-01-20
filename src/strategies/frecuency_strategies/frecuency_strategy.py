import os
from crontab import CronTab


class FrecuencyStrategy:
    _frequencies = {
        'daily': '0 0 * * *',  # Every day at midnight
        'weekly': '0 0 * * 0',  # Every Sunday at midnight
        'monthly': '0 0 1 * *',  # Every first day of the month at midnight
    }

    def set_frecuency(self):
        try:

            cron = CronTab(user='root')
            
            for job in cron.find_command('python /app/index.py'):
                cron.remove(job)
            
            job = cron.new(command='export IS_CRONJOB=true && python /app/index.py')
            
            if os.getenv('BACKUP_FREQUENCY') not in self._frequencies:
                raise ValueError(f"Invalid frequency: {os.getenv('BACKUP_FREQUENCY')}")

            backup_frequency = os.getenv('BACKUP_FREQUENCY')
            if backup_frequency in self._frequencies:
                job.setall('0 0 * * *')
            
            cron.write()
            print(f"Cron job set with frequency: {self._frequencies[backup_frequency]} ({os.getenv('BACKUP_FREQUENCY')})")
        except Exception as e:
            print(f"Error setting cron job: {e}")
            exit(1)