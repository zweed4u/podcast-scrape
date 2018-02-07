#!/usr/bin/python3
import json
import requests
import xmltodict

KFC = 'http://mcsorleys.barstoolsports.com/feed/kfc-radio'
TFTC = 'http://talesfromthecrypt.libsyn.com/rss'


class Podcast():
	def __init__(self, rss_urls):
		self.podcast_dict = {}
		self.rss_urls = rss_urls

	def build_dict(self):
		for podcast_url in self.rss_urls:
			xml = requests.request('GET', podcast_url).content
			data = xmltodict.parse(xml)
			pod_title = data['rss']['channel']['title']
			self.podcast_dict[pod_title] = {}
			episodes = data['rss']['channel']['item']
			for episode in episodes:
				try:
					self.podcast_dict[pod_title][f'{episode["title"]}'] = f'{episode["enclosure"]["@url"]}'
				except:
					#print(json.dumps(dict(episode), indent=4))
					continue
		return self.podcast_dict

print(json.dumps(Podcast([KFC, TFTC]).build_dict(), indent=4))
