import smtplib

# Envia un mail a mi cuenta principal de gmail
class Mail:

    def __init__(self, subj, body="", user="fakemail@gmail.com", password="contraseña"):

        gmail_user = user
        gmail_password = password

        sent_from = gmail_user
        to = ['stefanvallet99@gmail.com']

        email_text = 'Subject: {}\n\n{}'.format(subj, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()

            print('Email sent!')
        except Exception as e:
            print('Something went wrong...: ', e)


if __name__ == "__main__":
    Mail("perdio","perdio sin jugar", "fakemail@gmail.com", "contraseña")
