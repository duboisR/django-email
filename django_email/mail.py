from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend


class CustomEmailBackend(EmailBackend):
    def send_messages(self, messages):
        for message in messages:
            if settings.DEBUG:
                message.subject = "{subject} [{to}]".format(
                    subject=message.subject,
                    to=', '.join(message.to)
                )
                message.to = [settings.DEBUG_EMAIL]
        return super(CustomEmailBackend, self).send_messages(messages)
