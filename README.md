# astro_paper_template
This template serves as a starting point for papers being prepared for publication with [AAS](http://journals.aas.org/index.html) (e.g. Astronomy and Astrophysics, The Astrophysical Journal). The included `.cls` and `.bst` files are the most recent versions of [AASTeX](http://journals.aas.org/authors/aastex.html).

In addition to providing some basic templates, the main purpose of this project is to encourage *reproducible workflows* coupled with manuscript preparation. In other words, given some experiment or simulation data files, anyone should be able to click a button and build your paper **from scratch**.

The two main influences for this small project are:

* [Reproducible, One Button Workflows with the Jupyter Notebook & Scons | SciPy 2016 |Jessica Hamrick](https://www.youtube.com/watch?v=Fc2W930NJs8)
* [In Defense of Extreme Openness | Python in Astronomy 2016 | Jake VanderPlas](https://speakerdeck.com/jakevdp/in-defense-of-extreme-openness)
* [ewanmellor/gh-publisher | Configure an automated build and publish process with Travis CI and GitHub Pages](https://github.com/ewanmellor/gh-publisher)

## Using this template
This page is to merely serve as a skeleton for your own project. To set up your own project using this template:

1. Create new repository `<GitHubUsername>/my_new_paper` on [GitHub](https://github.com/)
2. Clone this repository into a folder `my_new_paper`
    ```Shell
    $ git clone https://github.com/wtbarnes/astro_paper_template.git my_new_paper
    ```
3. Reset the origin to your GitHub repository that you created in step 1.
    ```Shell
    $ git remote set-url origin https://github.com/<GitHubUsername>/my_new_paper.git
    ```
4. (optional) Add this repository as an upstream to keep up to date with any changes/improvements in the template
    ```Shell
    $ git remote add template https://github.com/wtbarnes/astro_paper_template.git
    ```
5. (optional) If you are collaborating with several people, it may be better to set the origin at a more centralized location and then have each individual user create a fork from that repository.

## Dependencies
The following are included in `requirements.txt`

* AstroPy
* ghp-import
* IPython
* Jupyter
* matplotlib
* NumPy
* pandas
* scons
* seaborn
* SciPy

and can be installed just using `pip install -r requirements.txt`. Additionally, you'll need [nbflow](https://github.com/jhamrick/nbflow) which is not currently available via PyPI. To install it,
```Shell
$ git clone https://github.com/jhamrick/nbflow.git
$ cd nbflow
$ python setup.py install
```

## Sample Workflow
