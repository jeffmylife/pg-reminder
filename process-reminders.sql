WITH due_reminders AS (
      SELECT id, reminder_text
      FROM reminders
      WHERE reminder_datetime <= NOW()
        AND NOT processed
    ),
http_requests AS (
    SELECT 
        due_reminders.id,
        net.http_post(
            url := 'https://pgreminder.loca.lt/hello',
            body := json_build_object('message', due_reminders.reminder_text)::jsonb
        ) AS request_id
    FROM due_reminders
),
http_responses AS (
    SELECT 
        http_requests.id,
        (net._http_response.content::jsonb) as response
    FROM http_requests
    JOIN net._http_response ON net._http_response.id = http_requests.request_id
),
processed_reminders AS (
    UPDATE reminders
    SET processed = TRUE
    FROM due_reminders
    WHERE reminders.id = due_reminders.id
    RETURNING reminders.id
)
UPDATE reminders
SET response_data = http_responses.response
FROM http_responses
WHERE reminders.id = http_responses.id
RETURNING reminders.id, reminder_text, response_data;