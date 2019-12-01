import Eval
import Reader

def int_read(arg):

    return Reader.read_str(arg)

def int_eval(arg, env):    

    if type(arg) != list:
        return Eval.eval_ast(arg, env)
    else:
        if len(arg) == 0:
            return arg
        else:
            buffer = Eval.eval_ast(arg, env)
            return buffer[0](buffer[1].data, buffer[2].data)

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
    line = input('user> ')
    buffer = int_read(line)
    repl_env = {'+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: int(a/b)}

    buffer = int_eval(buffer, repl_env)
    int_print(buffer)