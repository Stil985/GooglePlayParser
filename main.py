import requests
from bs4 import BeautifulSoup


def main():
    url = input("Введите необходимую ссылку:")
    response = requests.get(url=url)
    soap = BeautifulSoup(response.content, "lxml")
    soap.prettify()
    tags = soap.find(attrs={"data-g-id": "description"})
    for tag in tags.find_all('b'):
        tags.b.unwrap()
    for newlinews in tags('br'):
        tags.br.replace_with("\n")
    print(tags.get_text().strip())


if __name__ == '__main__':
    main()
