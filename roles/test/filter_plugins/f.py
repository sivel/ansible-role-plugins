class FilterModule(object):
    def filters(self):
        return {
            'foo': lambda x: 'FOO'
        }
