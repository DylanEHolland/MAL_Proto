from . import Env
from . import Eval
from . import Reader
from . import Types
from . import REPL_readline

def int_read(arg):

    return Reader.read_str(arg)

def int_eval(arg, env):    

    if type(arg) != list:
        return Eval.eval_ast(arg, env)
    elif len(arg) == 0:
        return arg
    elif len(arg) > 0:
        if callable(arg[0]):
            return Eval.apply(arg[0], [Eval.eval_ast(arg[1], env), Eval.eval_ast(arg[2], env)], env)
        elif arg[0].data == "def!":
            result = Eval.eval_ast(arg[2], env)
            result = int_eval(result, env)
            return env.set(arg[1].data, result)
        elif arg[0].data == "let*":
            new_env = Env.Env(outer = env)
            for n in range(0, len(arg[1]), 2):
                new_env.set(arg[1][n].data, arg[1][n+1].data)

            
            #return Eval.eval_ast(arg[2], new_env)
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

def repl():
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