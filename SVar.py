__author__ = 'eraldo.rangel'


class Svar:
    scene = None

    def __init__(self, name=None, ifilter=None):
        self.named = name
        self.filter = ifilter

    def match(self, x):
        if self.filter is None:
            if self.named is None:
                return {}
            return {self.named: x}
        return Svar.scene.match(self.filter, x)

    def __str__(self):
        return  "SVar("+ self.named+ ")"

    def __repr__(self):
        return  "SVar("+ self.named+ ")"