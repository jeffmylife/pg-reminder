# PG Reminder

PG Reminder is a lightweight solution designed to execute POST requests from a Supabase PostgreSQL database when a specified date has passed. It's a practical way to manage time-sensitive reminders or notifications directly from your database. This tool integrates Python scripts, SQL procedures, and Supabase, offering seamless functionality.

## Features

- **Automated POST Requests**: Triggers POST requests once reminders reach their due date.
- **Supabase Integration**: Works with Supabase for scheduling and managing reminders.
- **Simple Setup**: Minimal configuration required for local and cloud-based execution.
- **Open Source**: Fully customizable to meet your needs.

---

## Installation and Setup

### Prerequisites

- Python 3.13 (probably doesn't matter)
- Supabase account
- PostgreSQL database

### Clone the Repository

```bash
# Clone this repo
git clone https://github.com/jeffmylife/pg-reminder.git
cd pg-reminder
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Use

### 1. Start the Local Server

The local server listens for incoming POST requests.

```bash
python main.py
```

### 2. Expose the Server to the Internet

Use [localtunnel](https://theboroer.github.io/localtunnel-www/) to make your local server publicly accessible.

```bash
lt --port 8000 --subdomain pgreminder
```

### 3. Create the Reminder Table

Run the `create_reminder_table.py` script to set up the required database table.

```bash
python create_reminder_table.py
```

### 4. Insert Reminders

Add new reminders to the database by running the `insert_reminder.py` script. Customize the script to add specific reminders as needed.

```bash
python insert_reminder.py
```

### 5. Access the Database

To interact with your PostgreSQL database directly, run the `db-login.sh` script.

```bash
bash db-login.sh
```

---

## Automating Reminder Processing

To automate the processing of reminders, integrate the `process-reminders.sql` script into your Supabase project.

### Steps:

1. Open the SQL editor in Supabase.
2. Copy and paste the contents of `process-reminders.sql`.
3. Schedule the script to run as a cron job (e.g., every minute) within Supabase.

This setup ensures reminders are processed at regular intervals without manual intervention.

---

## Folder Structure

```
.
├── main.py                # Starts the local server
├── insert_reminder.py     # Inserts new reminders into the database
├── process-reminders.sql  # SQL logic to process reminders
├── create_reminder_table.py # Sets up the reminder table
├── db-login.sh            # Script for database login
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## Example Workflow

1. **Set Up the Server**: Start the local server and expose it via localtunnel.
2. **Create Reminders**: Insert reminders into the database using `insert_reminder.py`.
3. **Process Reminders**: Let the automated cron job handle reminders once their due dates are reached.
4. **Trigger Actions**: POST requests are sent to the specified URLs when reminders are processed.

---

## Contributing

Contributions are welcome! If you have ideas for improvement or want to report issues, please open an issue or create a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- Supabase for its powerful database and hosting solutions.
- Localtunnel for easy server exposure.

---

Happy reminding! 🚀

