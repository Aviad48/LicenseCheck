import time
import datetime
import logging
import os

# Ensure the log directory exists
log_dir = "/app/logs"
os.makedirs(log_dir, exist_ok=True)

# Set up logging
log_file = os.path.join(log_dir, "time_check.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def check_time_and_log():
    while True:
        now = datetime.datetime.now()

        # Check if the current time is on the hour
        if now.minute == 0 and now.second == 0:
            # If it's exactly on the hour, log "Task completed"
            hour_log_file = os.path.join(log_dir, f"{now.strftime('%Y-%m-%d_%H')}_task_completed.log")
            with open(hour_log_file, 'w') as f:
                f.write("Task completed")
            logging.info(f"Task completed for {now.strftime('%H:%M:%S')}")
        else:
            # If it's not on the hour, log "Incorrect time"
            hour_log_file = os.path.join(log_dir, f"{now.strftime('%Y-%m-%d_%H')}_incorrect_time.log")
            with open(hour_log_file, 'w') as f:
                f.write("Incorrect time")
            logging.info(f"Incorrect time for {now.strftime('%H:%M:%S')}")

        # Sleep for 5 seconds to wait until the next full Run
        time.sleep(5)

if __name__ == "__main__":
    check_time_and_log()
