import json
from ses_client import send

subject_file = open('./email/email_subject.txt', mode='r', encoding='UTF-8')
SUBJECT = subject_file.read()
subject_file.close()

body_file = open('./email/email_body.txt', mode='r', encoding='UTF-8')
BODY = body_file.read()
body_file.close()


def replace_text(text, key, value):
    target = '[!' + key + '!]'
    return text.replace(target, value)


def main():
    list_json = open('./email/email_list.json', mode='r', encoding='UTF-8')
    list_data = json.load(list_json)
    list_json.close()

    for item in list_data:
        # replace body
        body = BODY
        for key, value in item['replace'].items():
            body = replace_text(body, key, value)

        send(item['recipient'], SUBJECT, body)


if __name__ == '__main__':
    main()
