from ddns import DDNS


def main():
    ddns = DDNS("id", "token")
    ddns.update()


if __name__ == '__main__':
    main()
