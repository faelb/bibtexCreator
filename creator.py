from newsplease import NewsPlease
import pyperclip3
import base64
import hashlib

def crawlData(url):
    article = NewsPlease.from_url(url)
    return article
def main():
    #url = input("Enter url")
    url="https://www.smartinsights.com/social-media-marketing/social-media-strategy/new-global-social-media-research/"
    article = crawlData(url)
    #create a refIndex with a hash and use first 10 digits, to be sure its unique
    hash = hashlib.sha1(url.encode("utf-8"))
    refIndex = base64.urlsafe_b64encode(hash.digest()[:5]).decode("utf-8")

    #parse journal name out of URL
    if "www." in article.source_domain:
        journal = article.source_domain[4:]
    else:
        journal = article.source_domain

    #get authors or else journal is author
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
    year = article.date_publish.strftime("%Y")
    accessed = article.date_download.strftime("%d") +"." + article.date_download.strftime("%m") +"." +  article.date_download.strftime("%Y")






    blueprint = '@Article{'+refIndex+',\r\n  author  = {'+author+'},\r\n  journal = {'+journal+'},' \
                '\r\n  title   = {'+title+'},\r\n  year    = {'+year+'},\r\n  note    = {' \
                +accessed+'},\r\n  url     = {' \
                +url+'},\r\n} '

    print(blueprint)
    print("The bibtext was stored to your clipboard (use Ctrl V to paste it)")
    pyperclip3.copy(blueprint)

if __name__ == "__main__":
    main()
