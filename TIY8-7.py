def make_album(artist_name, album_title, songs=None):
    album = {'artist': artist_name.title(), 'title': album_title.title()}
    if songs: album['songs'] = songs
    return album

print(make_album("Ethan", "Python"))
print(make_album("Hallie", "Java"))
print(make_album("Amy", "C#"))

print(make_album("Vince", "Javascript", 10))
