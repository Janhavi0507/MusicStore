import random
import string

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_song_id_generator(instance):
    song_id = random_string_generator()

    klass = instance.__class__
    qs_exists = klass.objects.filter(AudioID=song_id).exists()
    if qs_exists:
        return random_string_generator(instance)
    return song_id
