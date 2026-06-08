import hashlib


def generate_hash(dom_content):
    """
    Generate SHA-256 hash of DOM content.
    """

    return hashlib.sha256(
        dom_content.encode("utf-8")
    ).hexdigest()


if __name__ == "__main__":

    sample_dom = """
    <html>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
    """

    hash_value = generate_hash(sample_dom)

    print("SHA-256 Hash:")
    print(hash_value)