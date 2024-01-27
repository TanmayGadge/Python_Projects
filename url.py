import urllib.request, urllib.parse, urllib.error


text = urllib.request.urlopen('https://en.wikipedia.org/wiki/Computer_science')
first_para = []
hit = False
condition = True
n = 0

links = []

while condition:
    for line in text:
        if('<p>' in line.decode()):
            hit = True
            first_para.append(line.decode())

        if('</p>' not in line.decode() and hit):
            first_para.append(line.decode())

        if('</p>' in line.decode() and hit):
            hit = False
            first_para.append(line.decode())
            break

    for element in first_para:
        if('href' in element):
            words = element.split('"')
            print(words[1])
            break
    
    if(words[1] not in links):
        links.append(words[1])
        text = urllib.request.urlopen('https://en.wikipedia.org/'+ words[1])
        first_para = []
    else:
        condition = False
    
