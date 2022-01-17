import pyshorteners


url = input("Enter a URL to short: ")
shorteners = pyshorteners.Shortener()
shorted_url = shorteners.tinyurl.short(url)
print(f"Your shorted URL is: {shorted_url}")
