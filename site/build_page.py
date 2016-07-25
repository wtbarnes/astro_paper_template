"""
Build a single-page website with Jinja2 to display our paper and some information about it.
"""

import os
import sys
import argparse

import jinja2
import yaml

class SinglePageSite(object):

    def __init__(self,site_config, site_template='site_template.html'):
        """Constructor"""
        self.site_template = site_template
        with open(site_config,'r') as f:
            self.yaml_config = yaml.load(f)

    def configure_env(self):
        """Set up the environment with the needed templates"""
        self.jenv = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')))

    def build_page(self,out_file=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output/index.html'), pdf_file='paper.pdf'):
        """Build page from template"""
        template = self.jenv.get_template(self.site_template)
        with open(out_file,'w') as f:
            f.write(template.render(info=self.yaml_config,pdf_file=pdf_file))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Build single-page website to display paper details')
    parser.add_argument('--config_file',help='paper and author info',default='project_config.yml')
    parser.add_argument('--pdf_file',help='PDF file path relative to printed html page')
    args = parser.parse_args()
    page_builder = SinglePageSite(args.config_file)
    page_builder.configure_env()
    if args.pdf_file is None:
        page_builder.build_page()
    else:
        page_builder.build_page(pdf_file=args.pdf_file)
