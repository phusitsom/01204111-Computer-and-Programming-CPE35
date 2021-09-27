def isPhotobook(s:str):
    global isPhoto
    isPhoto = s[0].isalpha() and s[-1].isalpha()
    return isPhoto

def hash(ch1:str, ch2:str):
    return ord(ch2)+10 if ch1>=ch2 else ord(ch1)-7

def calKey(string:str):
    return sum(hash(string[i], string[i+1])for i in range(len(string)-1))

def isPhotobookGenuine(key:int):
    if not isPhoto:
        return 'Incorrect Type'
    return not key%2

def isAlbumGenuine(key:int):
    if isPhoto:
        return 'Incorrect Type'
    return bool(key%2)

def solve():
    n = int(input())
    ids = [input() for _ in range(n)]
    real_photo_book = fake_album = 0
    for id in ids:
        isPhotobook(id)
        key = calKey(id)
        
        if isPhoto:
            if isPhotobookGenuine(key): 
                real_photo_book+=1
        else:
            if isAlbumGenuine(key): 
                fake_album+=1
    
    print(real_photo_book)
    print(fake_album)
