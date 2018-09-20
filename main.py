class Furniture():

    @staticmethod
    def factory(type):
        if type == 'chair':
            return _Chair()
        elif type == 'sofa':
            return _Sofa()
        else:
            raise ValueError('Unknown type: {}'.format(type))


class _Chair(Furniture):
    def __init__(self):
        self._name = 'chair'

    def __str__(self):
        return self._name


class _Sofa(Furniture):
    def __init__(self):
        self._name = 'sofa'

    def __str__(self):
        return self._name


if __name__ == '__main__':

    for product in ['chair', 'sofa']:
        print(Furniture.factory(product))
