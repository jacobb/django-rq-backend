from setuptools import setup

setup(
    name = "django-rq-backend",
    url = "http://github.com/jacobb/django-rq-backend",
    author = "Jacob Burch",
    author_email = "jacobburch@gmail.com",
    version = "0.1",
    packages = ["rq_task_backend"],
    description = "Redis Cache Backend for Django",
    install_requires=[
        "redis==2.8.0",
        "rq==0.3.11",
    ],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
