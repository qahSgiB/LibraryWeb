import importlib.util



class SafeDict(dict):
    def __missing__(self, key):
        return f'{{{key}}}'


class Template():
    def format(self, context):
        return None

class HtmlTemplate(Template):
    def __init__(self, template=None):
        self.template = template

    @staticmethod
    def templatePath(template):
        return f'page/htmlTemplates/{template}'

    @staticmethod
    def load(templateName):
        template = None

        with open(HtmlTemplate.templatePath(templateName), 'r') as templateFile:
            template = templateFile.read()

        return HtmlTemplate(template)

    def format(self, context):
        return self.template.format_map(SafeDict(context))

    def formatMultiple(self, contexts):
        html = ''
        for context in contexts:
            html += self.format(context)

        return html

class PyTemplate(Template):
    def __init__(self, renderFunc=None):
        self.renderFunc = renderFunc

    @staticmethod
    def load(pyTemplateName):
        templatePath = PyTemplate.templatePath(pyTemplateName)

        spec = importlib.util.spec_from_file_location('page/pyTemplates', templatePath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return PyTemplate(module.render)

    @staticmethod
    def templatePath(template):
        return f'page/pyTemplates/{template}'

    def format(self, context):
        return self.renderFunc(context)

    def formatMultiple(self, contexts):
        html = ''
        for context in contexts:
            html += self.format(context)

        return html
