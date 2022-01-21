import requests



website_url = input("Enter the Website URL to Extract all the Links: ")
response = requests.get(url=f"https://{website_url}").text
web_page = response


def crawl_url(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(a, b):
    for i in b:
        if i not in a:
            a.append(i)

def get_all_links(page):
    links_list = []
    while True:
        url, end_pos = crawl_url(page)
        if url:
            links_list.append(url)
            page = page[end_pos:]
        else:
            break
    return links_list 


def crawl_web(seed):
    to_crawl = [seed]
    crawled  = []
    while to_crawl:
        page = to_crawl.pop()
        if page not in crawled:
            union(to_crawl, get_all_links, crawl_url(page))
            crawled.append(page)

    return crawled


crawled_links = crawl_web(web_page)

print(f"The Links are: {crawled_links}")
