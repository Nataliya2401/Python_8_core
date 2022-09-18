import os
import re
import shutil
import sys


def normalize(name):

    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r",
                   "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    TRANS = {}
    for cyr_l, lat_l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(cyr_l)] = lat_l
        TRANS[ord(cyr_l.upper())] = lat_l.upper()

    name_translate = name.translate(TRANS)
    name_norm_file = re.sub('\W', '_', name_translate)

    return (name_norm_file)


# BASE_DIR = r'/Users/Natasha/Desktop/Motloh'

audio = (".amr", ".m4a", ".m4b", ".m4p", ".mp3",
         ".mpga", ".ogg", ".wav", ".wma")

documents = (".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx")

images = (".jpeg", ".png", ".jpg", ".svg")

video = (".avi", ".mp4", ".mov", ".mkv", ".wmv")

archives = (".zip", ".gz", ".tar")

list_directory_ignor = ['images', 'audio', 'video', 'documents', 'archives']

global folder
global list_ext_known
global list_ext_unnown

list_ext_known = []
list_ext_unnown = []


def make_dir(folder):
    # Create folders in root 'Motloh' for images, audio...

    global audio_path, video_path, documents_path, archives_path, image_path

    image_path = os.path.join(folder, 'images')
    audio_path = os.path.join(folder, 'audio')
    video_path = os.path.join(folder, 'video')
    documents_path = os.path.join(folder, 'documents')
    archives_path = os.path.join(folder, 'archives')

    if not os.path.exists(image_path):
        os.makedirs(image_path)

    if not os.path.exists(audio_path):
        os.makedirs(audio_path)

    if not os.path.exists(video_path):
        os.makedirs(video_path)

    if not os.path.exists(documents_path):
        os.makedirs(documents_path)

    if not os.path.exists(archives_path):
        os.makedirs(archives_path)


def check_empty_dir(name_dir):

    lists = os.listdir(name_dir)

    if not lists:
     #       print('not lost', lists)
        os.rmdir(name_dir)
    else:
        for file in lists:
            if not (file in list_directory_ignor):
                path_el = os.path.join(name_dir, file)
                if os.path.isdir(path_el):
                    check_empty_dir(path_el)


def sort_files(container):

    all_files = os.listdir(container)

    for file in all_files:

        # path to file|folder, wich must be sorted
        file_path = os.path.join(container, file)

        if os.path.isfile(file_path):  # if file - split ext, norm name and sorting

            name, ext = os.path.splitext(file)
            # split extention, normal name, add ext = new file name , normalize with ext
            file_n = normalize(name) + ext

            if ext in audio:
                os.replace(file_path, os.path.join(audio_path, file_n))
                if not (ext in list_ext_known):
                    list_ext_known.append(ext)
            elif ext in video:
                os.replace(file_path, os.path.join(video_path, file_n))
                if not (ext in list_ext_known):
                    list_ext_known.append(ext)

            elif ext in documents:
                os.replace(file_path, os.path.join(documents_path, file_n))
                if not (ext in list_ext_known):
                    list_ext_known.append(ext)

            elif ext in images:
                os.replace(file_path, os.path.join(image_path, file_n))
                if not (ext in list_ext_known):
                    list_ext_known.append(ext)

            elif ext in archives:
                # create folder in "archives" for unpacked arch_file with name arch_file
                name = normalize(name)
                path_for_archiv_in_archives = os.path.join(archives_path, name)

                if not os.path.exists(path_for_archiv_in_archives):
                    os.makedirs(path_for_archiv_in_archives)
                try:
                    shutil.unpack_archive(
                        file_path, path_for_archiv_in_archives)
                    print(f"Archive file {file_path} unpacked successfully.")

                except shutil.ReadError:
                    print(f"Archive {file_path} can't be unpack")
                    os.replace(file_path, os.path.join(
                        path_for_archiv_in_archives, file_n))
                else:
                    os.remove(file_path)

                if not (ext in list_ext_known):
                    list_ext_known.append(ext)

            else:
                if not (ext in list_ext_unnown):
                    list_ext_unnown.append(ext)
 #               print('  other')

        elif not (file in list_directory_ignor):

            dyrect_name_norm = normalize(file)
#            print('norm__direct', os.path.join(container, dyrect_name_norm))
            norm_direct = os.path.join(container, dyrect_name_norm)
            os.rename(file_path, norm_direct)
            sort_files(norm_direct)

    return (list_ext_known, list_ext_unnown)


def main():
    global folder

    if len(sys.argv) < 2:
        print('Enter path to folder which should be cleaned')
        exit()

    folder = sys.argv[1]
    print(folder)
    print(sys.argv)

    if not (os.path.exists(folder) and os.path.isdir(folder)):
        print('Path incorrect')

        exit()

#    folder = r'/Users/Natasha/Desktop/Motloh'

    make_dir(folder)
    list_exp, list_not_exp = sort_files(folder)
    print('sorted type of files', list_exp)
    print('not sorted type of files', list_not_exp)
    check_empty_dir(folder)


if __name__ == '__main__':
    main()
