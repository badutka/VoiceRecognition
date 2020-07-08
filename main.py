from jarvis_module import initializer, init_talk, queries


def main():
    engine = initializer()
    # while True:
    #     init_talk(engine)
    #     queries(engine)
    while True:
        init_talk(engine)


if __name__ == "__main__":
    main()
