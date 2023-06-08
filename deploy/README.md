# **GO OUTFIT**

[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-✨)

## **Table of Contents**

1. [Table of Contents](#table-of-contents)
2. [Project Overview](#project-overview)
3. [How to run this app](#how-to-run-this-app)
4. [Contributors](#contributors-✨)

## **Project Overview**

This app is a simple implementation of REST API and recommendation system. The datas are preprocessed using Tensorflow and Python. This REST API is built using Flask and containerized using Docker. The data images are stored in imagekit.io. Each data path is stored in a csv file that generated using Python and stored inside the app.

## **How to run this app**

### **Install Docker & create your account**

You can download and install Docker by going to this link:
[Download Docker Desktop](https://www.docker.com/products/docker-desktop/). Also, you can create a DockerHub account using this link: [DockerHub](https://hub.docker.com/) to be able to upload you containerized app into cloud storage.

### **Pull the image from DockerHub**

Once you've installed docker, you can use this command on terminal to pull the image of this app:

```bash
docker pull kuroyamii/flask-ml
```

### **Create environment file**

If you're going to run the container on your local computer, you can create an `.env` file and fill it with the environment variables. You can check the example on `.env.example`.

### **Create and run the container**

To run the container, you can simply use this command but with a little bit modification according to your needs:

```bash
docker run -d --name <your-container-name> --env-file <env-file-location> -p <your-desired-port>:8080 kuroyamii/flask-ml:latest
```

for example:

```bash
docker run -d --name flask-ml --env-file .env -p 8181:8080 kuroyamii/flask-ml:latest
```

### **Your app has successfully deployed!🎉**

After following above steps, finally you'll be able to access the app from your desired port. You can simply use your HTTP client app such as [Postman](https://www.postman.com/downloads/), [cURL](https://curl.se/), or your other favorite HTTP client to make request to the API.

## **Contributors ✨**

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center">
        <a href="https://github.com/kuroyamii">
            <img src="https://avatars.githubusercontent.com/u/76874550?v=4?s=100" width="100px;" alt=""/>
            <br />
            <sub>
                <b>
                Gede Gery Sastrawan
                </b>
            </sub>
        </a>
        <br />
        <a href="https://github.com/Go-Outfit/go-outfit-ml/commits?author=kuroyamii" title="Code">💻</a>
        <a href="https://github.com/Go-Outfit/go-outfit-ml/commits?author=kuroyamii" title="Documentation">📖</a>
        <a href="#infra-kuroyamii" title="Infrastructure">🚇</a>
        <a href="https://github.com/Go-Outfit/go-outfit-ml/pulls" title="Reviewed Pull Requests">👀</a>
    </td>
    <td align="center">
        <a href="https://github.com/citraandhini">
            <img src="https://avatars.githubusercontent.com/u/120680987?v=4?s=100" width="100px;" alt=""/>
            <br />
            <sub>
                <b>
                Citra Andhini
                </b>
            </sub>
        </a>
        <br />
        <a href="https://github.com/Go-Outfit/go-outfit-ml/commits?author=citraandhini" title="Code">💻</a>
        <a href="#citra-data" title="Data">📁</a>
    </td>
    <td align="center">
        <a href="https://github.com/dewiikumala">
            <img src="https://avatars.githubusercontent.com/u/103370489?v=4?s=100" width="100px;" alt=""/>
            <br />
            <sub>
                <b>
                Dewi Oka
                </b>
            </sub>
        </a>
        <br />
        <a href="https://github.com/Go-Outfit/go-outfit-ml/commits?author=dewiikumala" title="Code">💻</a>
        <a href="#dewi-data" title="Data">📁</a>
    </td>
  </tr>
</table>
