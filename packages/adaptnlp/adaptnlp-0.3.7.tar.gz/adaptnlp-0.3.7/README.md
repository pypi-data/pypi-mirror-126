# Welcome to AdaptNLP
> A high level framework and library for running, training, and deploying state-of-the-art Natural Language Processing (NLP) models for end to end tasks.


<p align="center">
    <a href="https://github.com/Novetta/adaptnlp"> <img src="https://raw.githubusercontent.com/novetta/adaptnlp/master/docs/assets/images/company_logo.png" width="400"/></a>
</p>

![CI](https://github.com/Novetta/adaptnlp/workflows/CI/badge.svg) 
[![PyPI](https://img.shields.io/pypi/v/adaptnlp?color=blue&label=pypi%20version)](https://pypi.org/project/adaptnlp/#description)

## What is AdaptNLP?

AdaptNLP is a python package that allows users ranging from beginner python coders to experienced Machine Learning Engineers to leverage
state-of-the-art Natural Language Processing (NLP) models and training techniques in one easy-to-use python package.

Utilizing [fastai](https://docs.fast.ai) with HuggingFace's [Transformers](https://github.com/huggingface/transformers) library and Humboldt University of Berlin's [Flair](https://github.com/flairNLP/flair) library, AdaptNLP provides Machine Learning Researchers and Scientists a modular and **adaptive** approach to a variety of NLP tasks simplifying what it takes to **train**, perform **inference**, and **deploy** NLP-based models and microservices.

## What is the Benefit of AdaptNLP Rather Than Just Using Transformers?

Despite quick inference functionalities such as the `pipeline` API in `transformers`, it still is not quite as flexible nor fast enough. With AdaptNLP's `Easy*` inference modules, these tend to be slightly faster than the `pipeline` interface (bare minimum the same speed), while also providing the user with simple intuitive returns to alleviate any unneeded junk that may be returned. 

Along with this, with the integration of the `fastai` library the code needed to train or run inference on your models has a completely modular API through the `fastai` [Callback](https://docs.fast.ai/callbacks.core) system. Rather than needing to write your entire torch loop, if there is anything special needed for a model a Callback can be written in less than 10 lines of code to achieve your specific functionalities.

Finally, when training your model fastai is on the forefront of beign a library constantly bringing in the best practices for achiving state-of-the-art training with new research methodologies heavily tested before integration. As such, AdaptNLP fully supports training with the One-Cycle policy, and using new optimizer combinations such as the Ranger optimizer with Cosine Annealing training through simple one-line fitting functions (`fit_one_cycle` and `fit_flat_cos`).

## Installation Directions

### PyPi

To install with pypi, please use:
```bash
pip install adaptnlp
```
Or if you have pip3:
```bash
pip3 install adaptnlp
```

### Conda (Coming Soon)

### Developmental Builds

To install any developmental style builds, please follow the below directions to install directly from git:

**Stable Master Branch**
The master branch generally is not updated much except for hotfixes and new releases. To install please use:
```bash
pip install git+https://github.com/Novetta/adaptnlp
```

**Developmental Branch**
{% include note.html content='Generally this branch can become unstable, and it is only recommended for contributors or those that really want to test out new technology. Please make sure to see if the latest tests are passing (A green checkmark on the commit message) before trying this branch out' %}
You can install the developmental builds with:
```bash
pip install git+https://github.com/Novetta/adaptnlp@dev
```

### Docker Images

There are actively updated Docker images hosted on Novetta's [DockerHub](https://hub.docker.com/r/novetta/adaptnlp)

The guide to each tag is as follows:

* **latest**: This is the latest pypi release and installs a complete package that is CUDA capable
* **dev**: These are occasionally built developmental builds at certain stages. They are built by the `dev` branch and are generally stable
* ***api**: The API builds are for the [REST-API](https://novetta.github.io/adaptnlp/rest)

To pull and run any AdaptNLP image immediatly you can run:
```bash
docker run -itp 8888:8888 novetta/adaptnlp:TAG
```
Replacing `TAG` with any of the afformentioned tags earlier.

Afterwards check `localhost:8888` or `localhost:888/lab` to access the notebook containers

## Navigating the Documentation

The AdaptNLP library is built with [nbdev](https://nbdev.fast.ai), so any documentation page you find (including this one!) can be directly run as a Jupyter Notebook. Each page at the top includes an "Open in Colab" button as well that will open the notebook in Google Colaboratory to allow for immediate access to the code.

The documentation is split into six sections, each with a specific purpose:

### [Getting Started](https://novetta.github.io/adaptnlp/)
This group contains quick access to the homepage, what are the AdaptNLP Cookbooks, and how to contribute

### [Models and Model Hubs](https://novetta.github.io/adaptnlp/model.html)
These contain any relevant documentation for the `AdaptiveModel` class, the HuggingFace Hub model search integration, and the `Result` class that various inference API's return

### Class API
This section contains the module documentation for the inference framework, the tuning framework, as well as the utilities and foundations for the AdaptNLP library.

### [Inference and Training Cookbooks](https://novetta.github.io/adaptnlp/cookbook.html)
These two sections provide **quick** access to *single use* recipies for starting any AdaptNLP project for a particular task, with easy to use code designed for that specific use case. 
There are currently over 13 different tutorials available, with more coming soon.

### [NLP Services with FastAPI](https://novetta.github.io/adaptnlp/rest)
This section provides directions on how to use the AdaptNLP REST API for deploying your models quickly with FastAPI

## Contributing

There is a controbution guide available [here](https://novetta.github.io/adaptnlp/contributing)

## Testing

AdaptNLP is run on the `nbdev` framework. To run all tests please do the following:

1. `pip install nbverbose`
2. `git clone https://github.com/Novetta/adaptnlp`
3. `cd adaptnlp`
4. `pip install -e .`
5. `nbdev_test_nbs`

This will run every notebook and ensure that all tests have passed. Please see the nbdev [documentation](https://nbdev.fast.ai) for more information about it. 

## Contact

Please contact Zachary Mueller at zmueller@novetta.com with questions or comments regarding AdaptNLP.

Follow  us on Twitter at [@TheZachMueller](https://twitter.com/TheZachMueller) and [@AdaptNLP](https://twitter.com/AdaptNLP) for
updates and NLP dialogue.

## License

This project is licensed under the terms of the Apache 2.0 license.
