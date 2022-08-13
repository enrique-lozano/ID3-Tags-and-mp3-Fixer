# ID3 Tags & mp3 Fixer 🎛️​🎶​

Fix your songs metadata, keep all metadata with the same ID3 version and better organize your library. Batch edit the names of your mp3 files, based on their metadata.

## Run it 🚀

To run the project you must have python 3 installed and added to your path. Once this step is done, you just have to clone the project, put the songs you want to edit in the folder called <code>input</code> and put this commands in the windows terminal, in the directory where you have cloned the project

```
pip install -r requirements.txt
```

```
python main.py
```

_You could try <code>python3</code> instead of <code>python</code> if the previous command does not work_

**Notes:**

> The project has been made with python version 3.10, so its compatibility with previous versions is not guaranteed.

> The program will skip files that are not in .mp3 format

## Settings ⚙️​

In the root folder of the project you will see a folder called <code>settings</code> file called <code>settings.json</code> inside. In this file, you can modify several parameters to your liking:

- **input_path**: Folder from which the mp3 files will be read. Defaults to "input"

- **output_path**: Folder in which the new fixed mp3 files will be downloaded. If this directory does not exist, it will be createdDefaults to "output"

- **id3_version**: Version of ID3 to use for the metadata. Check https://en.wikipedia.org/wiki/ID3 for more info

- **new_filename_format**: Format of the names that the new created files will have. You can specify song attributes in this name by putting them in square brackets. Defaults to "{album} - {title}". Accepted attributes are:

```
artist
title
album
discnumber
tracknumber
```

## Want to collaborate? 🙋🏻

Feel free to improve and optimize the existing code. To contribute to the project, read the previous points carefully and do the next steps with the project:

1. Fork it (<https://github.com/enriqueloz88/ID3-Tags-and-mp3-Fixer/fork>)
2. Create your feature branch (`git checkout -b feature/newFeature`)
3. Commit your changes (`git commit -am 'Add some newFeature'`)
4. Push to the branch (`git push origin feature/newFeature`)
5. Create a new Pull Request

## Need help ❓

Feel free to contact the developer if you have any questions or suggestions about the project or how you can help with it.
