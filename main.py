import requests
from datetime import timedelta, datetime, date


def get_questions():
    d = date.today() - timedelta(2)
    fromdate = int(datetime.timestamp(datetime(d.year, d.month, d.day)))
    page = 0
    num_article = 0
    while True:
        page += 1
        url = f'https://api.stackexchange.com/2.3/questions?page={page}&fromdate={fromdate}&order=desc&sort=activity&tagged=python&site=stackoverflow'
        res = requests.get(url).json()
        # Ограничение на 25 страниц
        if 'error_id' in res:
            break
        for record in res['items']:
            num_article += 1
            print(f'{num_article}) {record["title"]}')
        if res['has_more'] == 'false':
            break
    return num_article


if __name__ == '__main__':
    print('Список вопросов из stackoverflow по тегу python за последние 2 дня:')
    cnt_articles = get_questions()
    print(f'Количество загруженных вопросов: {cnt_articles}')
