# RISE for Jupyter Notebook Slides
- The [RISE extension](https://github.com/damianavila/RISE) allows a Jupyter Notebook to be played as a slideshow presentation.
- It uses [Reveal.js](https://github.com/hakimel/reveal.js) to convert notebook cells into javascript slides in the web browser.
- Metis has customized our own version of RISE (available [here](https://github.com/pburkard88/RISE)) to deliver lectures in the bootcamp.
- This document provides instructions for installing and configuring the Metis RISE extension so you can view notebooks as slideshows on your local machines.

## Background on Jupyter Extensions
- A variety of extensions can be installed to enhance the functionality of Jupyter Notebooks.  A bunch of them are available [here](https://github.com/ipython-contrib/jupyter_contrib_nbextensions) with instructions for installation.
- Usually one installs them as a complete package, but for our RISE extension you will follow the instructions below to install it in "developer mode" from the code source at [https://github.com/pburkard88/RISE](https://github.com/pburkard88/RISE)

## Installing Metis RISE
1. git Clone the repo at [https://github.com/pburkard88/RISE](https://github.com/pburkard88/RISE)
  - There are 2 ways to do this:
    1. Browse to [https://github.com/pburkard88/RISE](https://github.com/pburkard88/RISE) and click "Clone or Download".  Follow the instructions, installing GitHub Desktop if necessary/desired.
    2. Run `git clone https://github.com/pburkard88/RISE.git` from a command line terminal (assuming git has already been installed and configured)
2. Open a terminal and navigate to the `RISE` directory that was created (`cd <base_path>/RISE`)
3. Run `pip install -e .`
4. Run `jupyter-nbextension install rise --py --sys-prefix --symlink`
5. Run `jupyter-nbextension enable rise --py --sys-prefix`
6. To confirm that things have been installed correctly, start a Jupyter Notebook server via `jupyter notebook`, and open any Jupyter Notebook.  In the toolbar at the top of the notebook you should see a bar graph icon button (with 4 bars).  If you see this, then you've successfully installed the extension.
