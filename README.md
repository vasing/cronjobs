# Configuration

```
1. test_script.py - user paths
```

# Make The Python Script Executable

```bash
chmod +x /home/username/scripts/script.py
```

---

# Cron Tab Editor

Open the crontab editor for your user:
```bash
crontab -e
```

---

# Cron Syntax Explained

The cron syntax has five time fields:
```
* * * * * command_to_execute
│ │ │ │ │
│ │ │ │ └── Day of week (0-6, 0=Sunday)
│ │ │ └──── Month (1-12)
│ │ └────── Day of month (1-31)
│ └──────── Hour (0-23)
└────────── Minute (0-59)
```

For daily execution: `minute hour * * *`

---

# Add the Cron Job Entry

Add this line to schedule your script to run daily at a specific time:

## Option A: Run daily at 2:30 AM
```bash
30 2 * * * /usr/bin/python3 /home/username/scripts/script.py >> /home/username/scripts/logs/cron.log 2>&1
```

## Option B: Run daily at midnight (00:00)
```bash
0 0 * * * /usr/bin/python3 /home/username/scripts/script.py >> /home/username/scripts/logs/cron.log 2>&1
```

## Option C: Simple version (run at 6 AM)
```bash
0 6 * * * python3 /home/username/scripts/script.py
```

---

# Test the Cron Job

Temporarily set it to run in a few minutes:
```bash
# Replace your cron job with this temporarily
*/5 * * * * /usr/bin/python3 /home/username/scripts/test_script.py >> /home/username/scripts/logs/cron.log 2>&1
```
(This runs every 5 minutes for testing)