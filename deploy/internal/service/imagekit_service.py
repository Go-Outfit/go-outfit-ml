from imagekitio import ImageKit
from imagekitio.models.ListAndSearchFileRequestOptions import ListAndSearchFileRequestOptions


def get_file_list(imagekit: ImageKit):
    options = ListAndSearchFileRequestOptions(
        skip=0,
    )
    init = 0
    list_files = imagekit.list_files(options)
    for file in list_files.list:
        init += 1
    print(init)
