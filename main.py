def dayX():
    with (open('./dayX.txt')) as f:
        for line in f.readlines():
            print(line)


if __name__ == '__main__':
    dayX()
