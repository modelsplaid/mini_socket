

def print_flush(*values:object):
    print(values,flush=True)


if __name__ == '__main__':
    print_flush("hello",123,456)