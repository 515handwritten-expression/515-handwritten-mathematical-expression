from setuptools import setup
with open('requirements.txt') as f:
    required = f.read().splitlines()


opts = dict(name='Handwritten Mathematical Expression Recognition',
            maintainer='Summer Ai, Runting Shao, Ningji Shen, Chang Xu, Zihui Zhang',
            description='Handwritten Mathematical Expression Recognition Tool',
            long_description=('A website that recognize handwritten mathematical'
                              ' Expression, generate the printed version, and'
                              ' calculation result'),
            url='https://github.com/515handwritten-expression/515-handwritten-mathematical-expression',
            license='MIT',
            author='Summer Ai, Runting Shao, Ningji Shen, Chang Xu, Zihui Zhang',
            author_email='',
            version='1.0',
            install_requires=required,
            )

if __name__ == '__main__':
    setup(**opts)
