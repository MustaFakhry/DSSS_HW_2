from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List dependencies here if needed, e.g., 'numpy', 'pandas'.
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz',  
        ],
    },
    author="Mustafa Fakhry",
    author_email="mustafa.fakhry23@gmail.com",
    description="DSSS Homework_2",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/MustaFakhry/DSSS_HW_2",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
