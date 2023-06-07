import pkg.server.server as server
import pkg.bootstrapper.bootstrapper as bootstrapper
import pkg.config.config as config
from imagekitio.models.ListAndSearchFileRequestOptions import ListAndSearchFileRequestOptions
import internal.service.imagekit_service as imagekit_service

app = server.initialize_flask_app()

bootstrapper.initialize_routes(app)


# @app.route("/")
# def ping():
#     return "Hello World"
env = config.init_env_variables()
imagekit = config.init_imagekit_client(
    env.imagekit_public_key[0], env.imagekit_private_key[0], env.imagekit_endpoint_url[0])
imagekit_service.get_file_list(imagekit)


app.config['JSON_SORT_KEYS'] = False
app.run(port="8080")
