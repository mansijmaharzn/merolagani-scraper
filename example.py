from merolagani_scraper.merolagani import MeroLaganiScraper

scraper = MeroLaganiScraper()

print(scraper.scrape_company_details("GVL"))

print(scraper.scrape_lastest_ipo_news())
