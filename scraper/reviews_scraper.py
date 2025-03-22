import requests
from bs4 import BeautifulSoup


def get_reviews_from_page(page_num = 1):
    url = f"https://www.airlinequality.com/airline-reviews/british-airways/page/{page_num}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.content, "html.parser")

    reviews = []
    review_blocks = soup.find_all("div", class_ = "text_content")

    for block in review_blocks:
        review_text = block.getText(strip= True)
        reviews.append(review_text)

    return reviews


def get_reviews(pages = 3):
    all_reviews = []

    for page in range(1, pages + 1):
        print(f"Scraping page {page}...")

        reviews = get_reviews_from_page(page)
        all_reviews.extend(reviews)

    return all_reviews