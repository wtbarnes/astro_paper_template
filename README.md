# astro_paper_template
[![Build Status](https://travis-ci.org/wtbarnes/astro_paper_template.svg?branch=master)](https://travis-ci.org/wtbarnes/astro_paper_template)

As much a proof of concept as it is a template, this project combines the ideas of two existing projects, [nbflow](https://github.com/jhamrick/nbflow) and [gh-publisher](https://github.com/ewanmellor/gh-publisher), to allow others to openly produce publication-quality science with simple, reproducible workflows.

Run your paper with a single command through the power of [nbflow](https://github.com/jhamrick/nbflow), have it rebuilt at each commit (thanks to [Travs CI](https://travis-ci.org/)) and then published to [a clean and simple webpage](https://wtbarnes.github.io/astro_paper_template/). Others can simply view your current draft, offer feedback via GitHub issues, or download and build the paper themselves! astro_paper_template is meant to be simple and very configurable. It is not at all an original tool or concept, but rather brings together several great tools and ideas to allow for self-contained, reproducible workflows that produce publication-quality results.

This project includes `.cls` and `.bst` files from [AASTeX](http://journals.aas.org/authors/aastex.html), a set of templates used by publications like The Astrophysical Journal and Astronomy and Astrophysics. However, any TeX template can be used.

## Building this Example
Building this sample repository and the associated webpage yourself is very easy. Provided you have a working Python (2.7) and LaTeX installation, configure a virtual envrionment or [conda environment](http://conda.pydata.org/docs/using/envs.html), clone this repository in `$HOME/astro_paper_template` and run,
```Shell
$ pip install -r requirements.txt
$ git clone https://github.com/jhamrick/nbflow.git ../nbflow && cd ../nbflow
$ python setup.py install
$ cd astro_paper_template
$ scons
$ cd site && make
```
Navigate to `$HOME/astro_paper_template/site/output/index.html` to see the sample webpage. Check out the [example site](https://wtbarnes.github.io/astro_paper_template/) produced with this repository.

## Sample Workflow
1. Write your the text of your paper in LaTeX, including any custom TeX dependencies in the `tex/` subfolder.
2. Run analysis in Jupyter notebooks. Any prebuilt data files or figures should be placed in `results/static/`.
  1. Run `notebooks/make_math_plots.ipynb` and `notebooks/make_plot_from_exp_data.ipynb`
  2. Build table with `notebooks/make_table.ipynb`
  3. Run `notebooks/make_sim_data.ipynb`
  4. Build plots from output of step 2. with `notebooks/make_plot_from_sim_data.ipynb`
  6. Repeat steps when data files/notebooks change as necessary. **NOTE:** nbflow manages this for you.
3. Build the PDF of your paper. This can be included as a step in your `SConstruct` file.
4. Build and publish the current manuscript using `cd site && make`

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
6. Now add your own `.tex` file and notebooks and start writing your paper!
7. If you want automatic builds of your webpage, you may need to adjust `.travis.yml` and `requirements.txt` if you have different dependencies than those in this example. You'll also need to adjust `project_config.yml` appropriately so your webpage is accurate.

## Automatic Site Builds with Travis CI
[Travis CI](https://travis-ci.org/) is a continuous integration service that is easily configured as a GitHub webhook. Essentially, Travis will watch a branch of your repository and kick off builds (as described in the `.travis.yml` file) anytime it sees a new commit. In this case, Travis runs our analysis, compiles the TeX document and then publishes it all to a single webpage. To enable Travis builds for your repo, sign in with your GitHub account and click the switch for the appropriate repo.

The site is published via [GitHub Pages](https://pages.github.com/) so we'll need to create a `gh-pages` branch. This is where the site will live. Additionally, in order to allow Travis to push the site to this branch automatically, you'll need to configure your own [personal access token](https://help.github.com/articles/creating-an-access-token-for-command-line-use/) `GH_TOKEN`. The steps for properly encrypting it can be found [here](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html).

## Dependencies
The following are included in `requirements.txt`. Adjust them as needed for your project:

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

All of these packages (and their dependencies) can be installed just using `pip install -r requirements.txt`. Additionally, you'll need [nbflow](https://github.com/jhamrick/nbflow) which is not currently available via PyPI.

## Inspiration
The main influences for this small project are:

* [Reproducible, One Button Workflows with the Jupyter Notebook & Scons | SciPy 2016 | Jessica Hamrick](https://www.youtube.com/watch?v=Fc2W930NJs8)
* [In Defense of Extreme Openness | Python in Astronomy 2016 | Jake VanderPlas](https://speakerdeck.com/jakevdp/in-defense-of-extreme-openness)
* [ewanmellor/gh-publisher | Configure an automated build and publish process with Travis CI and GitHub Pages](https://github.com/ewanmellor/gh-publisher)
