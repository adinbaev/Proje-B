RASPBERRY_ID = 1

SYSTEM_STOPPED_DELAY_TIME = 5

DANGEROUS_WORD = "test"

DATABASE_FILE_NAME = "data/database.csv"
DATABASE_INDEX_NAME = 0
DATABASE_INDEX_EMAIL_ADDRESS = 1
DATABASE_INDEX_PHONE_NO = 2

WEBAPI_PROTOCOL = "http"
WEBAPI_HOST = "10.201.2.77"
WEBAPI_PORT = 37001

WEBAPI_URL = WEBAPI_PROTOCOL + "://" + WEBAPI_HOST + ":" + str(WEBAPI_PORT) + "/"

WEBAPI_URL_TEACHER = WEBAPI_URL + "api/teacher"
WEBAPI_URL_RASPBERRY = WEBAPI_URL + "api/raspberry/{}"

EMAIL_API_STMP_HOST = "smtp-mail.outlook.com"
EMAIL_API_SMTP_PORT = 587
EMAIL_API_EMAIL_ADDRESS = "muhammedtiftikci@outlook.com"
EMAIL_API_EMAIL_PASSWORD = ""

SMS_API_USERNAME = ""
SMS_API_ORIGINATOR = ""
SMS_API_PASSWORD = ""