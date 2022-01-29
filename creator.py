import pyperclip3


def main():
    refIndex = input("Enter refIndex")
    author = input("Enter author")
    journal = input("Enter journal")
    title = input("Enter title")
    year = input("Enter year")
    url = input("Enter url")
    accessed = "29.01.2022" #constant - set it yourself


    blueprint = '@Article{'+refIndex+',\r\n  author  = {'+author+'},\r\n  journal = {'+journal+'},' \
                '\r\n  title   = {'+title+'},\r\n  year    = {'+year+'},\r\n  note    = {' \
                +accessed+'},\r\n  url     = {' \
                +url+'},\r\n} '

    print(blueprint)
    print("The bibtext was stored to your clipboard (use Ctrl V to paste it)")
    pyperclip3.copy(blueprint)

if __name__ == "__main__":
    main()