# django_email
Mise en place d'un moteur de messagerie personnalisé Django avec redirection des e-mails en mode DEBUG

Python: 3.6.1  
Django: 2.0

## Installation

Mise en place de l'environnement de developpement.
```
virtualenv -p python3.6 venv
. venv/bin/activate
```

Récupération du dépôt Github.
```
git clone https://github.com/duboisR/django_email.git
cd django_email
pip install -Ur requirements.txt
```

## Test d'envoi d'email avec redirection en mode DEBUG

Avant de pouvoir faire notre premier test, il faut tout d'abord completer le fichier `settings.py`
avec vos paramètres d'authentification auprès du serveur SMTP.
```
EMAIL_HOST_USER = 'EMAIL_HOST_USER'
EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'
```

Test d'envoi d'e-mail en passant par l'interpréteur interactif Python de Django.
```
./manage.py shell
Python 3.6.3 |Anaconda, Inc.| (default, Oct  6 2017, 12:04:38) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.core.mail import send_mail
>>> send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
1
```

Si vous vous connectez sur Mailinator, vous devriez pouvoir visualiser l'e-mail qui a été redirigé dans la boîte mail de développement (django_email@mailinator.com).
