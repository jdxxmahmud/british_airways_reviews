from scraper.reviews_scraper import get_reviews

def main():
    print("Strting British Airways review scraper...\n")

    reviews = get_reviews(pages=5)

    print(f"Scraped {len(reviews)} reviews.\n")

    for i, review in enumerate(reviews, 1):
        print(f"{i}. {review}\n")

if __name__ == "__main__":
    main()