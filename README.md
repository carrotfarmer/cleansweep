![Cleansweep Logo](https://i.ibb.co/ky2y99F/Untitled-design.png)

# Cleansweep

Cleansweep is a tool that helps in cleaning your downloads folder and organizing files and directories.

## How it works

Cleansweep detects any download or file creation into your `Downloads` folder and moves them into specific directories depending on the file's type. These directories are specified in `settings.py`.

## Installation

```bash
git clone https://github.com/IQUBE-X/cleansweep.git
cd cleansweep
./build.sh
```

## Usage

Open `settings.py` and add the required data:

```py
# ADD CUSTOM DIRECTORIES HERE
DIRECTORY_TO_WATCH = ""
IMAGE_DESTINATION_FOLDER = ""
DOCUMENTS_DESTINATION_FOLDER = ""
MEDIA_DESTINATION_FOLDER = ""
CODE_DESTINATION_FOLDER = ""

# USE THIS PATH FOR OTHER DOWNLOAD TYPES
DESTINATION_FOLDER = ""

# GROUPS OF FILES BASEND ON THEIR
# RESPECTIVE FILE EXTENSIONS
# ADD EXTRA FILE TYPES HERE
IMAGES = [".png", ".jpg", ".webp", ".svg", ".bmp", ".gif"]
DOCUMENTS = [".pdf", ".docx", ".xlsx", ".csv", ".pptx"]
MEDIA = [".mp4", ".mp3", ".wav", ".mkv", ".mov"]
CODE = [".js", ".py", ".c", ".cpp", ".ts", ".h", ".hpp"]
```

- `DIRECTORY_TO_WATCH` should be locating to your `Downloads` folder.\
- `IMAGE_DESTINATION_FOLDER` maps to the folder where you want your image files to go to.
- `DOCUMENTS_DESTINATION_FOLDER` maps to the folder where you want your documents to go to.
- `MEDIA_DESTINATION_FOLDER` maps to the folder where you want your audio & video files to go to.
- `CODE_DESTINATION_FOLDER` maps to the folder where you want your code files to go to.

You can add more file types and create a destination folder for it. For eg:

```py
MY_CODE_FILES = [".rs", ".graphql", ".hs", ".scala", ".json"]

MY_CODE_FILES_DESTINATION = "F:\ME\Code"
```

or you can add more file types to the exisitng arrays.

After you add custom file types and create a destination for it, make sure you follow these steps:

1. Import it to `main.py`

```py
from settings import DIRECTORY_TO_WATCH, DESTINATION_FOLDER, IMAGE_DESTINATION_FOLDER, CODE_DESTINATION_FOLDER, MEDIA_DESTINATION_FOLDER, DOCUMENTS_DESTINATION_FOLDER, MEDIA, IMAGES, DOCUMENTS, CODE, MY_CODE_FILES, MY_CODE_FILES_DESTINATION
```

2. Add `MY_CODE_FILES` to the `ALL_CUSTOM_FILES` variable

```py
ALL_CUSTOM_FILE_TYPES = MEDIA + CODE + IMAGES + DOCUMENTS + MY_CODE_FILES
```

3. Add a `for` loop

```py
for my_code_file in MY_CODE_FILES:
    if my_code_file in event.dest_path:
        time.sleep(5)
        move_file(event.dest_path,
                  MY_CODE_FILES_DESTINATION)
        print(
            f"Moved {event.dest_path} to {MY_CODE_FILES_DESTINATION}")
```

Now, if a download has any extension from `MY_CODE_FILES` then it will automatically move the file to `MY_CODE_FILES_DESTINATION`

## Contributing

If you want to contribute to Cleansweep, please submit a **pull request**. And if you have come across any issues or bugs please open an issue.

## License

[MIT License](https://opensource.org/licenses/MIT)
