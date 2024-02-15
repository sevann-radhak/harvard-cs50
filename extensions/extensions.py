def main():
    file_name = input('File name: ')
    print(f'{file_media(file_name)}')

def file_media(file_name):
    file_name = file_name.lower().strip()
    extension = file_name.split('.')[-1]

    match extension:
        case 'gif':
            return 'image/gif'
        case 'jpeg' | 'jpg':
            return 'image/jpeg'
        case 'png':
            return 'image/png'
        case 'pdf':
            return 'application/pdf'
        case 'txt':
            return 'text/plain'
        case 'zip':
            return 'application/zip'
        case _:
            return 'application/octet-stream'


if __name__ == '__main__':
    main()
