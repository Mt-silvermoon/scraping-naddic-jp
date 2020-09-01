import requests
import bs4
import pickle
import os
import time

TARGET_URL = 'https://closers.naddicjapan.com/news/'
WEBHOOK_URL = 'DiscordなどのIncoming Webhook'
ARCHIVE_CACHE = './naddic_jp_news_cache.pkl'
FREQUENCY = 300

def get_article_list(url):
	_res = requests.get(url)
	_res.raise_for_status()
	_soup = bs4.BeautifulSoup(_res.text, "html.parser")
	_news_area = _soup.select('.sub_news_list_ul')[0]
	return _news_area.select('a')

def get_article(soup):
	if soup.find('span'):
		soup.find('span').decompose()
	_url = soup.get('href')
	_title = soup.h5.getText().strip()
	_category = soup.select('.sub_news_list_title')[0].getText().strip()
	return _category, _title, _url

def make_message(category, title, url):
	return '<'+category+'>'+title+' '+url

def send_message(message):
	main_content = {
	  "content": message
	}
	requests.post(WEBHOOK_URL, main_content)

def save_cache(cache):
	with open(ARCHIVE_CACHE, 'wb') as rc:
		pickle.dump(cache, rc)

def load_cache():
	with open(ARCHIVE_CACHE, 'rb') as rc:
		return pickle.load(rc)

while True:
	if not os.path.exists(ARCHIVE_CACHE):
		messages = []
		save_cache(messages)

	news_list = get_article_list(TARGET_URL)
	articles = [get_article(_) for _ in news_list]
	messages = [make_message(_[0], _[1], _[2]) for _ in articles]
	cache = load_cache()
	new_messages = [_ for _ in messages if not _ in cache]

	if new_messages:
		for _news in new_messages:
			send_message(_news)
			cache.append(_news)
		save_cache(cache)

	time.sleep(FREQUENCY)
