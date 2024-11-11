from setuptools import setup, find_packages

setup(
    name='tinytroupe',
    version='0.3.0',
    packages=find_packages(include=['tinytroupe', 'tinytroupe.*']),
    install_requires=[
        'pandas',
        'pytest',
        'openai>=1.40',
        'tiktoken',
        'msal',
        'rich',
        'requests',
        'chevron',
        'llama-index',
        'llama-index-embeddings-huggingface',
        'llama-index-readers-web',
        'pypandoc',
        'docx',
        'markdown',
        'jupyter',
    ],
    author='Paulo Salem',
    author_email='paulo.salem@microsoft.com',
    description='LLM-powered multiagent persona simulation for imagination enhancement and business insights.',
    url='https://github.com/microsoft/tinytroupe',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)