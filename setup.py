from setuptools import setup

setup(
    name='caesar_cipher',
    version='0.1',
    packages=['caesar_cipher', 'caesar_cipher.caesar_crypto_lib', 'caesar_cipher.caesar_runner_lib'],
    url='https://github.com/FilippoRanza/caesar_cipher.git',
    scripts=['script/caesar_cipher'],
    license='GPL3',
    author='Filippo Ranza',
    author_email='filipporanza@gmail.com',
    description='encrypt, decrypt and crack text file using Caesar Cipher'
)
