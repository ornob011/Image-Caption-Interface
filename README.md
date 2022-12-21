# Project Title

Interface of the [Image Caption Generator model](https://github.com/ornob011/Image-Caption-Generator)

## Table of Contents
- [Project Title](#project-title)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Usage](#usage)
  - [Installation](#installation)
  - [Contributing](#contributing)
  - [License](#license)

<div style="text-align: justify;">

## Introduction

It is an interface of the [model](https://github.com/ornob011/Image-Caption-Generator) to generate captions from an image. The interface was developed with simple HTML while Flask was utilized as the backend framework.

## Features

- Easy to use interface
- Real-time caption generating
- Integrated with Heroku
- Secure

## Usage

This `Usage` section provides detailed instructions on how to use the application, including how to run it, import it into your code, and use its various functions.

To use this application, follow these steps:

1. Run the following command in a terminal:
   
   ```
   python app.py
   ```
2. Look for the output of the terminal. The web link will be generated at [http://localhost:5000/](http://localhost:5000/)
   
3. Click on the link or copy-paste the link into the browser. An interface will come up.
   </br></br>
   ![interface](assets/interface.png)
   
   <p style="text-align:center">Figure: Web Interface</p>

4. Upload a image into the submit form of the web page.

5. In a few seconds (depending on the hardware), the prediction will come up in an interface. 
    </br></br>
    ![pred01](assets/pred_01.png)
    <p style="text-align:center">Figure: Almost correct prediction</p>

    </br>

    ![pred02](assets/pred_02.png)
    <p style="text-align:center">Figure: Correct prediction</p>


## Installation

To install this application, follow these steps:

1. Clone the repository to your local machine:
   
   ```
   git clone https://github.com/ornob011/Image-Caption-Interface.git
   ```

2. Navigate to the project directory:

    ```
    cd Image-Caption-Interface
    ```

3. Install the dependencies (for non-GPU):

    ```
    pip install -r requirements.txt
    ```

    Install the dependencies (for GPU): 

    ```
    pip install -r requirements-gpu.txt
    ```

4. Start the application:
   ```
   python app.py
   ```
   or 
   ```
   gunicorn app:app 
   ```
The application should now be running on your local machine.


## Contributing

I welcome contributions to this project! If you have an idea for a feature or improvement, or if you have found a bug, please feel free to open an issue in the [issue tracker](https://github.com/ornob011/Image-Caption-Interface/issues).

Before submitting a pull request, please make sure to:

- Read and follow our [contribution guidelines](CONTRIBUTING.md).
- Test your changes thoroughly.

Thank you for your contribution!


## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

MIT License

Copyright (c) 2022 Ornob Rahman

</div>