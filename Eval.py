from Types import (Symbol)

def eval_ast(arg, env):
    if type(arg) == list:
        buffer = []
        for node in arg:
            buffer.append(eval_ast(node, env))

        return buffer
    else:
        if arg.data_type == 'SYM':
            if arg.data in env:
                return env[arg.data]
        else:
            return arg