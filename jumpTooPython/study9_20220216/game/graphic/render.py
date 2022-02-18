#render.py
# from game.sound.echo import echo_test

#위의 import 해오는 방법과 동일한 것을 가져오는 것
from ..sound.echo import echo_test
def render_test():
    print("render")
    echo_test()