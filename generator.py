from jinja2 import Environment
import os
import shutil
from jinja2 import BaseLoader, TemplateNotFound
from os.path import join, exists, getmtime


class Loader(BaseLoader):
    def __init__(self, path):
        self.path = path

    def get_source(self, environment, template):
        path = join(self.path, template)
        if not exists(path):
            raise TemplateNotFound(template)
        mtime = getmtime(path)
        with open(path, 'r') as f:
            source = f.read()
        return source, path, lambda: mtime == getmtime(path)


class SourceBundle(object):
    def __init__(self, static_dir='static', src_dir='src', templates=None, dist_dir='dist'):
        if templates is None:
            self.templates = ['index.html']
        else:
            self.templates = templates

        self.static_dir = static_dir
        self.src_dir = src_dir
        self.dist_dir = dist_dir

    def _root(self):
        return os.path.dirname(os.path.abspath(__file__))

    def clean(self):
        if os.path.exists(self.dist_dir):
            shutil.rmtree(self.dist_dir)

    def build(self, **kwargs):
        if not os.path.exists(os.path.join(self._root(), self.dist_dir)):
            os.mkdir(os.path.join(self._root(), self.dist_dir))

        if self.static_dir is not None:
            if os.path.exists(os.path.join(self._root(), self.dist_dir, self.static_dir)):
                shutil.rmtree(os.path.join(self._root(), self.dist_dir, self.static_dir))
            shutil.copytree(
                os.path.join(self._root(), self.src_dir, self.static_dir),
                os.path.join(self._root(), self.dist_dir, self.static_dir)
            )

        env = Environment(loader=Loader(os.path.join(self._root(), self.src_dir)))
        for template in self.templates:
            with open(os.path.join(self._root(), self.dist_dir, template), 'w') as f2:
                slug = env.get_template(template)
                slug = slug.render(**kwargs)
                f2.write(slug)

        return True

if __name__ == '__main__':
    sb = SourceBundle(templates=[
        'index.html'
    ])
    sb.build()
