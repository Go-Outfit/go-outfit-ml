from imagekitio import ImageKit
import dotenv
import os


def init_imagekit_client(public_key, private_key, url):
    imagekit = ImageKit(
        public_key=public_key,
        private_key=private_key,
        url_endpoint=url
    )
    return imagekit


def init_env_variables():
    dotenv.load_dotenv()

    class EnvVariables:
        def __init__(self):
            self.imagekit_public_key = os.getenv("IMAGEKIT_PUBLIC_KEY"),
            self.imagekit_private_key = os.getenv("IMAGEKIT_PRIVATE_KEY"),
            self.imagekit_endpoint_url = os.getenv("IMAGEKIT_ENDPOINT_URL"),

    env = EnvVariables()
    return env
