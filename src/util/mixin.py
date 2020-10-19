
def glob(subdir='', pattern='**.py'):
    from glob import glob

    from config import path
    return glob(path.join(path.here, subdir, pattern))


def output(cmd):  # @see https://stackoverflow.com/a/2502883
    from subprocess import check_output
    out = str(check_output(cmd))
    start = out.rindex('\\n') + 2
    end = out.rindex('\'')
    return out[start:end]


def route(config_object, name=__name__):
    if name == '__main__':
        from os import getcwd, sep
        from sys import path as syspath  # @see https://stackoverflow.com/a/56999264
        from sys import version
        syspath.append('{}{}__pypackages__{}{}{}lib'.format(getcwd(), sep, sep, version[:3], sep))

    from util.flask import app, init_app
    init_app(config_object=config_object)

    if name == '__main__':
        from util.ui import UI
        UI().run(app=app)
    else:
        return app
