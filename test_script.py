#!/usr/bin/env python3
# /home/username/scripts/cron_notify.py

import os
import sys
import datetime
import subprocess
import json

def main():
    # Create detailed output
    output = [
        "=" * 60,
        f"SCRIPT EXECUTED - {datetime.datetime.now()}",
        f"Python Executable: {sys.executable}",
        f"Python Version: {sys.version.split()[0]}",
        f"Working Directory: {'home/unknown'}",
        f"User: {'unknown'}",
        f"Home Directory: {'home/unknown'}",
        f"PATH: {'unknown'}...",
        f"Process ID: {os.getpid()}",
        f"Parent Process ID: {os.getppid()}",
        "=" * 60,
        "✓ Script executed successfully!",
        "=" * 60
    ]
    
    # Print to stdout (will be captured by cron logs)
    for line in output:
        print(line)
    
    # Write to a log file
    log_dir = os.getcwd() + "/logs"
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, f"cron_test_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    with open(log_file, 'w') as f:
        f.write('\n'.join(output))
    
    print(f"\nLog saved to: {log_file}")
    
    # Try to send a desktop notification (if DISPLAY is available)
    try:
        notify_cmd = [
            'notify-send',
            'Cron Job Test',
            f'SCRIPT EXECUTED {datetime.datetime.now().strftime("%H:%M:%S")}\nSee {log_file} for details',
            '-t', '5000'  # Display for 5 seconds
        ]
        subprocess.run(notify_cmd, check=False)
    except:
        pass  # Notification not available, that's OK
    
    # Also create a simple popup using zenity if available
    # Try to display a popup notification using zenity (if available)
    #try:
        # popup_cmd = [
        #     'zenity', '--info',
        #     '--title', 'SCRIPT EXECUTED',
        #     '--text', f'Cron job executed!\nTime: {datetime.datetime.now()}\nPython: {sys.executable}\nLog: {log_file}',
        #     '--width', '400',
        #     '--height', '200'
        # ]
        # subprocess.run(popup_cmd, check=False)
        # except:
        # pass  # zenity not available

if __name__ == "__main__":
    main()