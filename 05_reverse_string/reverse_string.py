def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    boo =(list(phrase))
    boo.reverse()
    return ''.join(boo)
