from ddns import DDNS


def main():
    ddns = DDNS("72982", "395fdff0dd5035f04734e9a679a9ece5")
    ddns.update()


if __name__ == '__main__':
    main()
