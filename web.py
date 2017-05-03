import os, sys
import cherrypy
import service

upload_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__))), 'upload')

def prepare_dir():
    if not os.path.isdir(upload_dir):
        os.makedirs(upload_dir)

if __name__ == '__main__':
    enable_ssl = False
    if len(sys.argv) > 1 and sys.argv[1] == 'ssl':
        enable_ssl = True

    prepare_dir()

    server_config = {
        'server.socket_port':5000,
        'server.socket_host':'0.0.0.0'
    }
    if enable_ssl:
        server_config.update({
            'server.socket_port':5001,
            'server.ssl_module':'pyopenssl',
            'server.ssl_certificate':'ssl.crt',
            'server.ssl_private_key':'ssl.key'
        })

    cherrypy.config.update({'server.socket_port':5000})
    conf = {
        '/upload':{
            'tools.staticdir.on':True,
            'tools.staticdir.dir':upload_dir
        }
    }
    cherrypy.quickstart(service.web_service(), config=conf)
