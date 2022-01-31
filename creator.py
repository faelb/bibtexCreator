from datetime import date

from newsplease import NewsPlease
import pyperclip3
import base64
import hashlib


def crawlData(url):
    article = NewsPlease.from_url(url)
    return article


def main():
    url = input("Enter url")
    # url="https://www.smartinsights.com/social-media-marketing/social-media-strategy/new-global-social-media-research/"
    article = crawlData(url)
    # create a refIndex with a hash and use first 10 digits, to be sure its unique
    hash = hashlib.sha1(url.encode("utf-8"))
    refIndex = base64.urlsafe_b64encode(hash.digest()[:5]).decode("utf-8")

    # parse journal name out of URL
    if "www." in article.source_domain:
        journal = article.source_domain[4:]
    else:
        journal = article.source_domain

    # get authors or else journal is author
    author = ""
    if len(article.authors) == 0:
        author = journal
    else:
        if len(article.authors) == 1:
            author = article.authors[0]
        else:
            for element in article.authors:
                author += element + " and "
            author = author[:-5]

    title = article.title
    try:
        year = article.date_publish.strftime("%Y")
    except:
        year = "2022"
    try:
        accessed = article.date_download.strftime("%d") + "." + article.date_download.strftime(
            "%m") + "." + article.date_download.strftime("%Y")
    except:
        accessed = date.today().strftime("%d") + "." + date.today().strftime("%m") + "." + date.today().strftime("%Y")

    print("please confirm or change the parameters:")
    print(f"author = {author}")
    userinput = input("change author? type in author now or press Enter")
    if userinput:
        author = userinput
    print("")
    print("")
    print(f"journal = {journal}")
    userinput = input("change journal? type in journal now or press Enter")
    if userinput:
        journal = userinput
    print("")
    print("")
    print(f"title = {title}")
    userinput = input("change title? type in title now or press Enter")
    if userinput:
        title = userinput
    print("")
    print("")
    print(f"year = {year}")
    userinput = input("change year published? type in year now or press Enter")
    if userinput:
        year = userinput

    print("-------------------------------------------------")
    print("")
    print("This is your Bibtex:")
    print("")
    print("")
    blueprint = '@Article{' + refIndex + ',\r\n  author  = {' + author + '},\r\n  journal = {' + journal + '},' \
                                                                                                           '\r\n  title   = {' + title + '},\r\n  year    = {' + year + '},\r\n  note    = {' \
                + "accessed: " + accessed + '},\r\n  url     = {' \
                + url + '},\r\n} '

    print(blueprint)
    print("")
    print("")
    print("-------------------------------------------------")
    print("The bibtext was stored to your clipboard (use Ctrl V to paste it)")
    pyperclip3.copy(blueprint)


if __name__ == "__main__":
    main()
