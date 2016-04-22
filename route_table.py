import webapp2
import sys
import logging
# from bottle import Bottle, request
from orator import DatabaseManager, Model
from Config.config import Config
from FileHelper.file_helper import FileHelper
#import controllers#
from Controllers.users_controller import UsersController

db = DatabaseManager(Config.get_config(self=0))
Model.set_connection_resolver(db)

class route_router(webapp2.RequestHandler):
    def get(self, controller, method, other):
        # select
        logging.info('GET request controller: ' + controller + ' method: ' + method + ' other: ' + other)
        response_string = self.exec_command(controller=controller, method=method, other=other)
        self.response.write(response_string)

    def post(self, controller, method, other):
        # insert
        logging.info('POST request controller: ' + controller + ' method: ' + method + ' other: ' + other)
        response_string = self.exec_command(controller=controller, method=method, other=other)
        self.response.write(response_string)

    def put(self, controller, method, other):
        # update
        logging.info('POST request controller: ' + controller + ' method: ' + method + ' other: ' + other)
        response_string = self.exec_command(controller=controller, method=method, other=other)
        self.response.write(response_string)

    def delete(self, controller, method, other):
        logging.info('POST request controller: ' + controller + ' method: ' + method + ' other: ' + other)
        response_string = self.exec_command(controller=controller, method=method, other=other)
        self.response.write(response_string)

    def exec_command(self, controller, method, other="", input=None):
        try:
            if input is None:
                    if other != "":
                        return eval(controller + "." + method + "('" + other + "')")
                    else:
                        return eval(controller + "." + method + "()")
            else:
                return eval(controller + "." + method + "(" + input + ")")
        except:
            logging.error('%s', sys.exc_info())



def handle_404(request, response, exception):
    logging.warning('HTTP 404: The following url is not defined: ' + request.path)
    response.set_status(404)

application = webapp2.WSGIApplication([
    webapp2.Route('/<controller>/<method>/<other>', handler=route_router, name='top-level router')

    ])

application.error_handlers[404] = handle_404

