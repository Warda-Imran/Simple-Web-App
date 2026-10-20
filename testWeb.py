
from pathlib import Path
from html.parser import HTMLParser
import unittest


class WebsiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.ids = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        self.ids.extend(
            value for name, value in attrs if name == "id"
        )


class TestWebsite(unittest.TestCase):
    def test_html_file_exists(self):
        self.assertTrue(Path("index.html").is_file())

    def test_css_file_exists(self):
        self.assertTrue(Path("style.css").is_file())

    def test_html_has_title(self):
        html = Path("index.html").read_text(encoding="utf-8")
        parser = WebsiteParser()
        parser.feed(html)

        self.assertIn("title", parser.tags)

    def test_html_has_body(self):
        html = Path("index.html").read_text(encoding="utf-8")
        parser = WebsiteParser()
        parser.feed(html)

        self.assertIn("body", parser.tags)


if __name__ == "__main__":
    unittest.main()
