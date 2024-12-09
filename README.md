# Supabase Postgres Reminder

A way to run POST requests to a server from a Supabase Postgres database based on whether or not a date is in the past.

## Local Run

```bash
# start server to receive messages
python main.py
```

```bash
# expose our local server to the internet for testing 
lt --port 8000 --subdomain pgreminder
```

```bash
# insert a reminder into the database
python insert_reminder.py
```

```bash
bash db-login.sh 
```

## Supabase 

### Cron Job to run process reminders

Copy the process-reminders.sql file to the Supabase SQL editor and run it as a cron job