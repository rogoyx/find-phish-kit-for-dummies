import urllib
import requests


def look_for_phishing(data):
    file_names = dict()
    file_index = 0
    for i, raw_url in enumerate(data):
        if raw_url[-1] != '/':
            raw_url = raw_url + '/'
        raw_url = raw_url[::-1]
        for i in range(1, len(raw_url)):
            if raw_url[i-1] == '/' or raw_url[i-1] == '.':
                raw_url = raw_url[::-1]
                if raw_url[:-i] == 'https://' or raw_url[:-i] == 'http:' or raw_url[:-i] == 'https:/' or raw_url[:-i] == 'https:' or raw_url[:-i] == 'http://' or raw_url[:-i] == 'http:/':
                    break
                for j in range(1, 5):
                    if j == 1:
                        extension = '.zip'
                    elif j == 2:
                        extension = '.rar'
                    elif j == 3:
                        extension = '.tar'
                    elif j == 4:
                        extension = '.tar.gz'
                    url = raw_url[:-i] + extension
                    try:
                        b = requests.get(url)
                        if b.status_code == 200:
                            r = requests.get(url)
                            file_index += 1
                            file_name = "file-{}{}".format(file_index, extension)
                            with open("C:\\Users\\andom\\архивы\\{}".format(file_name), "wb") as code:
                                code.write(r.content)
                                file_names[file_name] = url
                                with open("results.txt", "a") as results:
                                    results.write("{} {}\n".format(file_name, url))
                    except (requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
                        pass
                raw_url = raw_url[::-1]


if __name__=='__main__':
    data = urllib.request.urlopen("https://openphish.com/feed.txt").read()
    data = data.decode("utf-8")
    data = data.split('\n')
    data = data[:-1]
    look_for_phishing(data)

