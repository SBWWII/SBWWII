import smtplib
from email.mime.text import MIMEText

# Email details
sender_email = "your_email@example.com"
participant_email = "participant@example.com"
static_email = "sbwwiiroundtable@gmail.com"
subject = "Confirmation Email"
body = "Thank you for signing up!"

# Create email message
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = participant_email
msg["CC"] = static_email  # Add the static email

# Send email
with smtplib.SMTP("smtp.example.com", 587) as server:
    server.starttls()  # Indented 4 spaces
    server.login(sender_email, "your_password")  # Indented 4 spaces
    server.sendmail(sender_email, [participant_email, static_email], msg.as_string())  # Indented 4 spaces

print("Confirmation email sent!")