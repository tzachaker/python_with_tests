import requests

def fetch_website(url):
    response = requests.get(url)
    return response.status_code

if __name__ == "__main__":
    url = "https://www.example.com"
    print(f"Status code for {url}: {fetch_website(url)}")
