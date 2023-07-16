[Add effective prject logo or banner]: #
<p align="center">
  <img src="" alt="project logo" />
</p>


[Choose a self-explaining name for your project.]: #
<p align="center">Human, Dog and Cat Faces Detection</p>

[Add short description (one sentance)]: #


## 📂Table of Contents
- [�Table of Contents](#table-of-contents)
- [📋Project Description](#project-description)
- [📊Features](#features)
- [⛏️Built Using](#️built-using)
  - [🎫Prerequisites](#prerequisites)
- [📝Usage](#usage)
- [✍Authors](#authors)
- [💳License](#license)
- [🏅Acknowledgments](#acknowledgments)

## 📋Project Description
The project aims to develop a computer vision system that can accurately identify and distinguish between human, dog, and cat faces in images or videos. By utilizing advanced algorithms and machine learning techniques.

## 📊Features 
- Human face detection
- Dog face detection
- Cat face detection

## ⛏️Built Using
- [Python](https://www.python.org/): Programming language


### 🎫Prerequisites
You need the following python library:
- [OpenCV](https://opencv.org/): 4.8.0
```
pip install opencv-python==4.8.0
```

## 📝Usage
You can just run the file.
<br>
To change the model you need to provide your model and set the path to it, in the following part of the code:
```
# Load the HAAR Cascade face detection models
human_cascade = cv2.CascadeClassifier('models\human-model\myfacedetector.xml')
cat_cascade = cv2.CascadeClassifier('models\cat-model\haarcascade_frontalcatface.xml')
dog_cascade = cv2.CascadeClassifier('models\dog-model\haarcascade_frontalface_alt.xml')
```

## ✍Authors
- [@Afnan-Algogandi](github.com/afnanAlgogandi)
- [@Mohammed-Dhabaab](github.com/mohammed-dhabaab)


## 💳License
- [MIT](https://opensource.org/license/mit/)

## 🏅Acknowledgments
- [EVC](evc.sa)
- [Eng.Ibrahem Saber](https://www.linkedin.com/in/ibrahem-elnawasany/)

- [Avelino](https://github.com/avelino): Provided the dog model
- [Murtaza Hassan](https://github.com/murtazahassan): Provided the cat model