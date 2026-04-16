from email.message import EmailMessage
import smtplib

msg = EmailMessage()
msg['Subject'] = 'Hello from Docker'
msg['From'] = '<from@gmail.com>'
msg['To'] = '<to@gmail.com>'
msg.set_content('Everything is fine. EHLO success')

# Использовать localhost 25 (Настраивается в Docker)
with smtplib.SMTP(host='localhost', port=25) as smtp_server:
    # ehlo (Extended Hello) — это команда, которой твой Python-скрипт "здоровается" с почтовым сервером.
    smtp_server.ehlo()  # Здороваемся
    # starttls() и login() пропускаем, так как наш smtp4dev их не требует
    smtp_server.send_message(msg)
    print('Email was sent!')
