import Env
import Eval
import Reader
import REPL_readline

def int_read(arg):

    return Reader.read_str(arg)

def int_eval(arg, env):    

    if type(arg) != list:
        return Eval.eval_ast(arg, env)
    elif len(arg) == 0:
        return arg
    elif len(arg) > 0:
        if arg[0].data == "def!":
            result = Eval.eval_ast(arg[2], env)
            return env.set(arg[1].data, result)
        else:
            buffer = Eval.eval_ast(arg, env)
            return Eval.apply(buffer[0], [buffer[1], buffer[2]], env)

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

if __name__ == "__main__":
    repl_env = Env.Env()
    while True:
        line = REPL_readline.readline()
        buffer = int_read(line)
        repl_env.set('+', lambda a,b: a+b)
        repl_env.set('-', lambda a,b: a-b)
        repl_env.set('*', lambda a,b: a*b)
        repl_env.set('/', lambda a,b: a/b)

        buffer = int_eval(buffer, repl_env)
        int_print(buffer)