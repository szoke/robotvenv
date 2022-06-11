import aszokepackage.aszokemodule
from aszokepackage.aszoke_class_holder import AszokeClass
from robot.api.deco import keyword

my_class = AszokeClass()

@keyword()
def create_once():
    aszokepackage.aszokemodule.do_cool_stuff()
    return 'test user'

@keyword()
def load_webpage(url):
    return my_class.do_http_get(url).content
