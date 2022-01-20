import requests


website_url = input("Enter the Website URL to Extract all the Links: ")
response = requests.get(url=f"https://{website_url}").text
page = response


def crawl_url(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def print_all_links(page):
    while True:
        url, end_pos = crawl_url(page)
        if url:
            print(url)
            page = page[end_pos:]
        else:
            break 


print("The Links are: ")
print_all_links(page)
