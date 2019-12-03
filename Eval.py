from Types import (Symbol)
import Reader
import main

def apply(f, args):
    if isinstance(args[0], Reader.MalData):
        args[0] = args[0].data

    if isinstance(args[1], Reader.MalData):
        args[1] = args[1].data

    return f(args[0], args[1])

def eval_ast(arg, env):
    if type(arg) == list:
        buffer = []
        for node in arg:
            buffer.append(main.int_eval(node, env))

        return buffer
    else:
        if arg.data_type == 'SYM':
            #if arg.data in env.data:
            return env.get(arg.data)
        else:
            return arg