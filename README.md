# readtome

#### A CLI to read code via intelligent text-to-speech

Have you ever wanted to listen to your code just as you would any audiobook or podcast? Have you ever run your code through a traditional text-to-speech tool and forced yourself to listen to the chainsaw wail that emerged? I have, and my ears are still recovering. Fortunately, thanks to the magic of modern AI we can now generate coherent and listenable audio from raw code.

This project offers a CLI tool that will read an arbitrary file as audio. Just run `readtome file <file>` and your code will be instantly transformed into code you can listen to on your commute, run, or while you're doing the dishes. (Okay, it's not instant, but it's close!)

**Work in progress - contributors welcome!**

## Project Features

* [readtome](http://readtome.readthedocs.io/)
* [Click](http://click.pocoo.org/5/) command-line application
* automated unit tests you can run with [pytest](https://docs.pytest.org/en/latest/)
* a [Sphinx](http://www.sphinx-doc.org/en/master/) documentation project

## Getting Started

To use this tool, set these local environment variables:

* `OPENAI_API_KEY`
* `ELEVENLABS_API_KEY`

This will work best with a paid plan on each.

Install `mvp` for streaming audio: `sudo apt install mvp`.

Run the command line tool:

* `readtome --help`: Show usage information
* `readtome <filename>`: Translate the given file into audio

The project's documentation contains a section to help you
[get started](https://readtome.readthedocs.io/en/latest/getting_started.html) as a developer or
user of the library.

## Development Prerequisites

If you're going to be working in the code (rather than just using the library), you'll want a few utilities.

* [GNU Make](https://www.gnu.org/software/make/)
* [Pandoc](https://pandoc.org/)

## Resources

Below are some handy resource links.

* [Project Documentation](http://readtome.readthedocs.io/)
* [Click](http://click.pocoo.org/5/) is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary.
* [Sphinx](http://www.sphinx-doc.org/en/master/) is a tool that makes it easy to create intelligent and beautiful documentation, written by Geog Brandl and licnsed under the BSD license.
* [pytest](https://docs.pytest.org/en/latest/) helps you write better programs.
* [GNU Make](https://www.gnu.org/software/make/) is a tool which controls the generation of executables and other non-source files of a program from the program's source files.


## Authors

* **Josh Winters** - *Initial work* - [github](https://github.com/jbwinters)

See also the list of [contributors](https://github.com/jbwinters/readtome/contributors) who participated in this project.

## LicenseMIT License

Copyright (c) jbwinters

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
