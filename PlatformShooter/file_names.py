from os import walk, path

def find_files(folder):
    folder = path.join('Assets', folder)

    surf_list = []
    for _, __, filename in walk(folder):
        for image in filename:

            surf_list.append(image)

    return surf_list





