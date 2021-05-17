import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from settings import CREDENTIALS_FILE, SPREADSHEET_ID


def main():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, [
        'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

    httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
    # Выбираем работу с таблицами и 4 версию API
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
    sheet = service.spreadsheets()
    print('https://docs.google.com/spreadsheets/d/' + SPREADSHEET_ID)

    # Получаем список листов, их Id и название
    # spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheetId).execute()
    # sheetList = spreadsheet.get('sheets')
    # for sheet in sheetList:
    #     print(sheet['properties']['sheetId'], sheet['properties']['title'])

    # sheetId = sheetList[0]['properties']['sheetId']

    range_name = 'Лист1!A:C'
    result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID, range=range_name).execute()
    values = result.get('values', [])
    if values:
        for row in values:
            print('%s, %s' % (row[0], row[1]))
    else:
        print('No data found.')


if __name__ == '__main__':
    main()
