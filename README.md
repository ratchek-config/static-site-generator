# A very simple static site generator
When pelican and jekyll are overkill, and all you really need is an easy way to utilize Jinja2 template inheritance, this should do the trick.

# Setup
Clone the repo  
`git clone git@github.com:ratchek-config/static-site-generator.git`

Change into the directory  
`cd static-site-generator`

Create a virtual environment  
`python3 -m venv env`

Activate the virtual environment  
`source env/bin/activate`

Install Jinja2  
`pip install Jinja2`


# How to use
The general structure of your project should be:

```
static-site-generator
├── generator.py
├── README.md
└── src
    ├── static
    │   └── static_files_or_folders
    │   └── static_files_or_folders
    │   └── static_files_or_folders
    └── templates
        └── template_1
        └── template_2
        └── template_3
```


Put any static files you have in the static dir, and any templates in the templates folder. Pretty self explanatory.  
Add any templates you want generated to the template_list in `settings.py`.
(You don't want to generate *all* templates unless you're literally not using any Jinja inheritance or `include` statements)
Then make sure the virtual environment is activated and run  
`python generator.py`


Your site will be generated in a folder called `output` in the project root. Copy the contents of that folder to whatever hosting site you're using et voilà!

# More
Read more about Jinja2 syntax here:  
https://jinja.palletsprojects.com/en/3.0.x/templates/

Inspired (and a lot of code just copied outright) by  
https://www.pybloggers.com/2016/03/a-really-minimal-static-website-generator-with-python-and-jinja2/
