def make_album(artist_name, album_title):
    return {'artist': artist_name.title(), 'title': album_title.title()}


while True:
    artist = input("Artist: ")
    if artist == "q": break
    title = input("Title: ")
    if title == "q": break

    print(make_album(artist, title))
