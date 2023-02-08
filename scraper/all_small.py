import requests
from MyParser import Parser


def main():
    '''
    the algorithm:
    1. buka file small_links.txt
    2. untuk setiap line, parse websitenya di beautiful soup
        parse: judul, soal, pilihan, solusi
    3. simpan hasil setiap line dalam sebuah folder tersendiri
    '''

    LINK_DIR = "small_links.txt"
    HTML_FILE = "../../../../../Desktop/101.html"
    links = list()

    with open(LINK_DIR, "r") as file:
        lines = file.readlines()
        for line in lines:
            links.append(line[:-1])

    parser = Parser()
    options = parser.parse_opt(HTML_FILE)
    solutions = parser.parse_solution(HTML_FILE)
    questions = parser.parse_questions(HTML_FILE)


if __name__ == '__main__':
    main()
