from zipfile import ZIP_DEFLATED, ZipFile


def create_empty_zip():
    with ZipFile("metanit.zip", "w") as myzip:
        pass


def add_file_to_zip():
    with ZipFile(
        "metanit.zip", "a", compression=ZIP_DEFLATED, compresslevel=3
    ) as myzip:
        myzip.write("hello2.txt")


def list_info_files():
    with ZipFile("metanit.zip", "r") as myzip:
        for item in myzip.infolist():
            print(
                f"File Name: {item.filename} "
                f"Date: {item.date_time} "
                f"Size: {item.file_size}"
            )


def get_info():
    with ZipFile("metanit.zip", "r") as myzip:
        try:
            hello_file = myzip.getinfo("hello2.txt")
            print(hello_file.file_size)
        except KeyError:
            print("Указанный файл отсутствует")


def extract_list_files():
    with ZipFile("metanit.zip", "r") as myzip:
        myzip.extractall()  # если все в текущую папку
        # myzip.extractall(path="metanit2", members=["hello.txt", "forest.jpg"])


def read_file_without_extract():
    with ZipFile("metanit.zip", "r") as myzip:
        content = myzip.read("hello2.txt")
        print(content)


def open_file_without_extract():
    with ZipFile("metanit.zip", "a") as myzip:
        # записываем в архив новый файл "hello5.txt"
        with myzip.open("hello5.txt", "w") as hello_file:
            encoded_str = bytes("Python...", "UTF-8")
            hello_file.write(encoded_str)


# create_empty_zip()
# add_file_to_zip()
# list_info_files()
# get_info()
# extract_list_files()
# read_file_without_extract()
# open_file_without_extract()
