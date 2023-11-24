import sys, tempfile, os
from subprocess import call

def read_from_editor(initial_msg: str):
    EDITOR = os.environ.get('EDITOR', 'vim')

    with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
        tf.write(initial_msg.encode())
        tf.flush()
        call([EDITOR, tf.name])

        tf.seek(0)

        return tf.read()
