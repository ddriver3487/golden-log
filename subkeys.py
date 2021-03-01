ukeys = [
    "Application-Name",
    "Application-Version",
    "Author",
    "Creation-Date",
    "Document ImageModificationTime",
    "File Modified Date",
    "File Size",
    "Image Height",
    "Image Width",
    "Last-Author",
    "Last-Modified",
    "Last-Save-Date",
    "creator",
    "dc:format",
    "language",
    "producer",
    "publisher",
    "resourceName",
    "title",
    "version",
    "width",
    "height",
    "xmpDM:album",
    "xmpDM:albumArtist",
    "xmpDM:artist",
    "xmpDM:compilation",
    "xmpDM:composer",
    "xmpDM:discNumber",
    "xmpDM:duration",
    "xmpDM:genre",
    "xmpDM:releaseDate",
    "xmpDM:trackNumber",

]

lowerkeys = list()
for k in ukeys:
    k = k.lower()
    lowerkeys.append(k)
