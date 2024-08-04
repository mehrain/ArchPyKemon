import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

class BDParser:
    def __init__(self):
        self.entries = []

    def crawl_data(self):
        url = 'https://boot.dev/leaderboard'
        response = requests.get(url)
        self.html = response.text

    def save_html(self, file_path):
        with open(file_path, 'w') as file:
            file.write(self.html)

    def parse_html(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        arcanum_section = soup.find('h2', string='Archmage Arcanum').find_parent('div', class_='px-4')

        if arcanum_section is None:
            print("Error: 'Archmage Arcanum' section not found on the webpage.")
            exit(1)

        for item in arcanum_section.find_all('div', class_='glassmorph'):
            rank = item.find('span', class_='text-xl').text.strip()
            name = item.find('p', class_='truncate').text.strip()
            username = item.find('p', class_='text-left').text.strip()
            date = item.find('span', class_='ml-3').text.strip()
            self.entries.append((rank, name, username, date))

    def sort_entries(self):
        self.entries.sort(key=lambda x: datetime.strptime(x[3], '%m/%d/%Y'))

    def reassign_ranks(self):
        sorted_entries = []
        for i, entry in enumerate(self.entries, start=1):
            sorted_entries.append(f"Rank: {i}, Name: {entry[1]}, Username: {entry[2]}, Date: {entry[3]}")
        self.entries = sorted_entries

    def write_to_csv(self, file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Rank', 'Name', 'Username', 'Date'])
            for entry in self.entries:
                writer.writerow(entry.split(', '))

    @staticmethod
    def start():
        parser = BDParser()
        parser.crawl_data()
        parser.save_html('/home/mehrain/Workspace/github.com/mehrain/ArchPyKemon/src/parses/BDraw.html')
        parser.parse_html()
        parser.sort_entries()
        parser.reassign_ranks()
        parser.write_to_csv('/home/mehrain/Workspace/github.com/mehrain/ArchPyKemon/src/parses/BDparsed.csv')

BDParser.start()