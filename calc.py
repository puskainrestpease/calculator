# -*- coding: utf-8 -*-

try:
    import time
    import os
    from termcolor import cprint
    cprint(r'All modules ok!', 'green')
    time.sleep(0.5)
    os.system('clear')
except ModuleNotFoundError or ImportError as er:
    exit(f'{er}\ncheck out imports!')


if __name__ == '__main__':
    try:
        print(eval(input(f'''Input here you'r example: ''')))
    except Exception as er:
        if 'unexpected EOF while parsing (<string>, line 0)' or 'unexpected EOF while parsing (<string>, line 1)' in er:
            cprint(r'You wrote the example wrong!', 'red')
        else:
            cprint(r'An unexpected exception has occurred!', 'yellow')
