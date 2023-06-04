import pkg.server.server as server
import pkg.bootstrapper.bootstrapper as bootstrapper

app = server.initialize_flask_app()

bootstrapper.initialize_routes(app)


# @app.route("/")
# def ping():
#     return "Hello World"

app.config['JSON_SORT_KEYS'] = False
app.run(port="8080")
