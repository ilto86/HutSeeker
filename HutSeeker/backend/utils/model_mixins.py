class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_length(cls):
        return max(len(name) for name, _ in cls.choices())