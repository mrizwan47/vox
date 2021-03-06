# vox

[![Build Status](https://travis-ci.org/mrizwan47/vox.svg?branch=master)](https://travis-ci.org/mrizwan47/vox)
[![Gitter chat](https://badges.gitter.im/python-vox/Lobby.png)](https://gitter.im/python-vox/Lobby)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![License: MIT](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://opensource.org/licenses/MIT)

Simple Text to Voice API for Python and Command Line

## Installation

Requirements:
* Windows or Linux (macOS untested)
* Python 3+ or Python 2.7

Install this module from pypi using `pip3` (or `pip2` for Python 2):

```bash
$ pip3 install git+https://github.com/mrizwan47/vox
```

## Usage

#### Command-Line Interface

~~When you install `vox`, you get a simple command-line program
called `vox` that you can use to make your program say the text.~~

I'm new to Python and it's currently working by initiating `python -m`:

```bash
$ python -m vox "hello world"
```

Also, there's a second argument for language

```bash
$ python -m vox "Hola Mundo" es
```

#### Python Module

You can import the `vox` module and then easily use `say` function to give your program speaking ability.

```python
import vox

# Says 'Hello World' in english
vox.say( 'Hello World' )

# Says 'Hola Mundo' in Spanish
vox.say( 'Hola Mundo', 'es' )

```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Uses [gTTS](https://github.com/pndurette/gTTS/)
