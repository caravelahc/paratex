import urllib.request


def main():
    test = load_html("https://www.google.com/")
    print(test)


def load_html(url: str):
    html = urllib.request.urlopen(url)
    return html.read()


if __name__ == '__main__':
    main()
