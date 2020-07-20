# SES Template Sender

Send emails from template using AWS SES.

## Install Requirements
```
pip install -r requirements.txt
```

To use `Boto`, create the AWS credential file. ([link](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/create-shared-credentials-file.html))

## Configure Emails

The configuration files are in `email`.

* `email_config.json` : AWS SES configurations
* `email_list.json` : List of recipients and their replacement texts.
* `email_subject.txt` : Subject of email
* `email_body.txt` : Body of email

Texts that look like `[!something!]` in `email_body.txt` are automatically changed to the replacements in `email_list.json` for each recipient.

## Send Emails
```
python send_email.py
```
