import bs4
from django.core.management.base import BaseCommand, CommandError
import requests
import re
from lyrics.models import Song, Verse

class Command(BaseCommand):

    def get_lyric_page_urls(self):
        url = 'http://www.metrolyrics.com/abba-alpage-3.html'
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text)
        regex = re.compile(".*lyrics.*")
        elements = soup.findAll('a', {'title': regex})
        return [a.attrs.get('href') for a in elements]

    def get_lyrics_data(self, url):
        data = {}
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text)
        try:
            data['title'] = soup.select('h1')[0].get_text()[1:-8]
            data['verses'] = [p.get_text() for p in soup.select('div#lyrics-body-text p.verse')]
            data['acks'] = [p.get_text() for p in soup.select('p.writers')]
        except:
            pass
        return data

    def handle(self, *args, **options):
        """
        Get the list of urls, then parse each into Song and Verses
        """
        for url in self.get_lyric_page_urls():
            data = self.get_lyrics_data(url)

            if 'title' in data:
                try:
                    Song.objects.get(title=data['title'])
                except:
                    song = Song(title=data['title'], writers='\n'.join(data['acks']))
                    song.save()

                    for verse in data['verses']:
                        v = Verse(verse_text=verse, song=song)
                        v.save()
