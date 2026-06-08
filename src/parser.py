from bs4 import BeautifulSoup


def extract_dom(html_content):
    """
    Parse HTML and return normalized DOM structure.
    """

    soup = BeautifulSoup(
        html_content,
        "lxml"
    )

    return soup.prettify()


if __name__ == "__main__":

    sample_html = """
    <html>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
    """

    dom = extract_dom(sample_html)

    print(dom)