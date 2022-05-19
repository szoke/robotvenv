from robot.api.deco import keyword
import boto3
import aszokepackage.aszokemodule

@keyword()
def create_once():
    aszokepackage.aszokemodule.cool()
    return 'test user'
