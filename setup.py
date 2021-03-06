import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytorch_vision_classifier",
    version="0.0.10",
    author="sammer sallam",
    author_email="samersallam92@gmail.com",
    description="This library is to help you train and evaluate PyTorch classification model easily and quickly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Samer92/pytorch_vision_classifier",
    packages=["pytorch_vision_classifier"],
    install_requires=['backcall==0.2.0', 'classification-analysis==0.0.2', 'colorama==0.4.3', 'cycler==0.10.0', 
                      'decorator==4.4.2', 'imbalanced-learn==0.7.0', 'imblearn==0.0', 'ipython==7.16.1', 
                      'ipython-genutils==0.2.0', 'jedi==0.17.1', 'joblib==0.15.1', 'kiwisolver==1.2.0', 
                      'matplotlib==3.2.2', 'numpy==1.19.0', 'opencv-python==4.2.0.34', 'pandas==1.0.5',
                      'parso==0.7.0', 'pickleshare==0.7.5', 'Pillow==7.1.2', 'prompt-toolkit==3.0.5', 
                      'Pygments==2.6.1', 'pyparsing==2.4.7', 'python-dateutil==2.8.1', 'pytz==2020.1', 
                      'scikit-learn==0.23.1', 'scipy==1.5.0', 'seaborn==0.10.1', 'six==1.15.0', 
                      'threadpoolctl==2.1.0', 'tqdm==4.46.1', 'traitlets==4.3.3', 'wcwidth==0.2.5'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)