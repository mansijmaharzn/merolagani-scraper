import requests
from bs4 import BeautifulSoup


def get_company_details(symbol):
    base_url = "https://merolagani.com/CompanyDetail.aspx?symbol="
    url = base_url + symbol

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print("Error occurred during the request:", e)
        return None


def parse_company_general_details(soup):
    tbodies = soup.find_all('tbody')

    for tbody in tbodies:
        tr = tbody.find('tr')
        th = tr.find('th') # heading
        td = tr.find('td') # value


        if th.text.strip() == "% Dividend":
            break

        td_text = td.get_text(strip=True)
        if td_text:
            print(f"{th.text.strip()}: {td_text}")
        else:
            print("Invalid Symbol")
            break


def main():
    query_symbol = input("Enter Symbol to see details: ").upper()
    soup = get_company_details(query_symbol)
    
    if soup:
        parse_company_general_details(soup)


if __name__ == "__main__":
    main()
