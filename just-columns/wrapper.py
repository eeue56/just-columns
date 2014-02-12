import tornado.web
import tornado.ioloop
import tornado.concurrent

import logging

path_maps = {
    
}


class get(object):
    def __init__(self, path):
        global path_maps
        self.path = path
        path_maps[path] = self
        self.function = None

        
    def __call__(self, *args, **kwargs):
        print('recalling')

        if len(args) > 0:
            self.function = args[0]
        
        print('function is ', self.function.__name__)
        
        def func(self_, *args, **kwargs):
            print('being called..')
            stuff = self.function()
            self_.write(stuff)
            print('written')
            return stuff

        if len(args) < 1:
            pass #return None# tornado.concurrent.return_future(func)


        return func


def paths_to_handlers():
    global path_maps

    handlers = []

    for path, handler in path_maps.items():
        handler_class = type(path, 
            (tornado.web.RequestHandler, object), 
            dict(get=handler))

        handlers.append((path, handler_class))

    return handlers



def run(port_number=80):

    logging.info('Adding handlers')
    application = tornado.web.Application(paths_to_handlers())
    
    logging.info('Listening on port {}'.format(port_number))
    application.listen(port_number)

    logging.info('Main loop starting')
    tornado.ioloop.IOLoop.instance().start()
