import requests
from melipayamak import Api

def send_verification_code(phone_number, verification_code):
    username = '09022241854'  # نام کاربری ملی پیامک
    password = 'Ilia.arshia123@'  # رمز عبور ملی پیامک
    api = Api(username, password)
    sms = api.sms()
    _from = '50002710041854'  # شماره فرستنده
    text = f'کد تایید شما {verification_code} میباشد'

    try:
        response = sms.send(phone_number, _from, text)
        print("Response:", response)

        # بررسی وضعیت ارسال پیامک
        if response.get('RetStatus') == 1:
            print("SMS sent successfully.")
        else:
            print(f"Failed to send SMS. Status: {response.get('StrRetStatus')}")
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")


def send_sms_to_admin(message):
    username = '09022241854'  # نام کاربری ملی پیامک
    password = 'Ilia.arshia123@'  # رمز عبور ملی پیامک
    api = Api(username, password)
    sms = api.sms()
    _from = '50002710041854'  # شماره فرستنده
    recipient = "09369516811"  # شماره تلفن مدیر
    text = f'پیام جدید از سایت شما: {message}'

    try:
        response = sms.send(recipient, _from, text)
        print("Response:", response)

        # بررسی وضعیت ارسال پیامک
        if response.get('RetStatus') == 1:
            print("SMS to admin sent successfully.")
        else:
            print(f"Failed to send SMS to admin. Status: {response.get('StrRetStatus')}")
    except Exception as e:
        print(f"Error sending SMS to admin: {str(e)}")


def new_ticket_notif(message):
    username = '09022241854'  # نام کاربری ملی پیامک
    password = 'Ilia.arshia123@'  # رمز عبور ملی پیامک
    api = Api(username, password)
    sms = api.sms()
    _from = '50002710041854'  # شماره فرستنده
    recipient = "09369516811"  # شماره تلفن مدیر
    text = f'پیام جدید از سایت شما: {message}'

    try:
        response = sms.send(recipient, _from, text)
        print("Response:", response)

        # بررسی وضعیت ارسال پیامک
        if response.get('RetStatus') == 1:
            print("SMS to admin sent successfully.")
        else:
            print(f"Failed to send SMS to admin. Status: {response.get('StrRetStatus')}")
    except Exception as e:
        print(f"Error sending SMS to admin: {str(e)}")

