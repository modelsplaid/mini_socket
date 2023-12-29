from setuptools import setup, find_packages


setup(name            ='Mini socket',
      version         ='0.0.0',
      description     ='To pass message between clients and server through TCP',
      url             ='git@github.com:modelsplaid/mini_socket',
      author          ='Zhiqiang Tang',
      author_email    ='1457311565@qq.com',
      license         ='MIT',
      packages        =find_packages(),
      install_requires=["argcomplete"],
      zip_safe        =False
      )
