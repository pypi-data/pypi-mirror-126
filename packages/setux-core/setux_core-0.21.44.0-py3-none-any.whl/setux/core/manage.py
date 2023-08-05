from inspect import cleandoc

from pybrary.func import todo

from setux.logger import info


# pylint: disable=no-member


class Manager:
    def __init__(self, distro, quiet=False):
        self.distro = distro
        self.target = distro.target
        self.run = self.target.run
        self.key = None
        self.quiet = quiet

    @staticmethod
    def is_supported(distro):
        return True

    @classmethod
    def help(cls):
        for klass in (
            c
            for c in cls.mro()
            if issubclass(c, Manager)
        ):
            try:
                return cleandoc(klass.__doc__)
            except: pass
        return '?'

    def __str__(self):
        base = self.__class__.__bases__[0].__name__
        return f'{base}.{self.manager}'


class Checker(Manager):
    def fetch(self, key, *args, **spec):
        self.key = key
        self.args = args
        self.spec = self.validate(spec)
        return self

    def __call__(self, key, *args, **spec):
        self.fetch(key, *args, **spec)
        self.deploy()
        return self

    def validate(self, specs):
        return {
            k : v
            for k, v in self.do_validate(specs)
        }

    def do_validate(self, specs): todo(self)

    def deploy(self, msg=''):
        status = f'{"." if self.set() else "X"}'
        if not self.quiet:
            if msg: msg = f'{msg}:\n'
            info(f'{msg}\t{self.manager} {self.key} {status}')
        return status=='.'

    def __str__(self):
        fields = ', '.join(f'{k}={v}' for k, v in self.get().items())
        return f'{self.manager}({fields})'


class SpecChecker(Checker):
    def chk(self, name, value, spec):
        return value == spec

    def check(self):
        data = self.get()
        if data:
            for k, v in self.spec.items():
                # if data.get(k) != v:
                if not self.chk(k, data.get(k), v):
                    return False       # mismatch
            return True                # conform
        return None                    # absent

    def set(self):
        ok = self.check()
        if ok:
            return ok
        else:
            if ok is None:
                self.cre()
            data = self.get()
            if not data: return None
            for k, v in self.spec.items():
                if not self.chk(k, data.get(k), v):
                    self.mod(k, v)
                    data = self.get()
            return self.check()


class ArgsChecker(Checker):
    def check(self):
        data = self.get()
        if data:
            for arg in self.args:
                if arg not in data:
                    return False       # mismatch
            return True                # conform
        return None                    # absent

    def set(self):
        data = self.get()
        for arg in data:
            if arg not in self.args:
                self.rm(arg)
        for arg in self.args:
            if arg not in data:
                self.add(arg)
        return self.check()
