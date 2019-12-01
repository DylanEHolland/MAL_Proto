import Reader   

def int_read(arg):
    return Reader.read_str(arg)

def int_eval(arg):
    return arg

def int_print(arg):
    print(Reader.pr_str(arg))

def rep(arg):
    int_print(
        int_read(
            int_eval(
                arg
            )
        )
    )

while True:
    line = input('user>')
    buffer = int_read(line)
    int_print(buffer)