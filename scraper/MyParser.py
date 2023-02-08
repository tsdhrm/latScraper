from bs4 import BeautifulSoup
from string import ascii_lowercase, punctuation
import re


class Parser:
    def parse_opt(self, html_file) -> list:
        """ Metode kelas Parser untuk ekstrak pilihan ganda

        Args:
            html_file (str): lokasi file .html 

        Returns:
            list: pilihan ganda untuk tiap-tiap soal 
        """
        all_options = list()  # list to collect all available options
        file = open(html_file, "r")
        soup = BeautifulSoup(file, 'lxml')
        # print(soup.prettify())
        all_divs = soup.find("div", {"class": 'postBody'}).find_all(
            "ul", {"class": None})  # get only 'ul' in a 'div' that has class 'postBody'

        for div in all_divs:
            options = dict()
            for index, d in enumerate(div):
                # remove <li> and </li> tags with whitespace and remove whitespaces
                text = re.sub('<.*?>', '', str(d)).strip()
                options[str(ascii_lowercase[index])] = text
            all_options.append(options)
        file.close()
        return all_options

    def parse_solution(self, html_file: str) -> list[str]:
        """Parsing solutions form HTML file

        Args:
            html_file (str): HTML file directory 

        Returns:
            list: Lists of solutions
        """
        solutions = list()
        with open(html_file, 'r') as hfile:
            soup = BeautifulSoup(hfile, 'lxml')
            items = soup.findChildren("div", {
                'style': '-moz-border-radius: 10px; -webkit-border-radius: 2px; background-color: #e1f5fe; border-radius: 4px; padding: 10px; t-align: left;'})

            for item in items:
                texts = ''
                if item.div:
                    texts = item.div.text
                else:
                    texts = item.text
                solutions.append(texts.translate(
                    str.maketrans('', '', punctuation)).lower()[-1])

        return solutions

    def parse_questions(self, html_file: str) -> list[str]:
        """Parse questions from HTML file

        Args:
            html_file (str): HTML file directory

        Returns:
            list[str]: List of questions
        """
        print("hi")
        return ['Hello']
