class Template():
    def __init__(self, template=None):
        self.template = template

    def load(templateName):
        template = None

        with open(templatePath(templateName), 'r') as templateFile:
            template = templateFile.read()

        return Template(template)

    def format(self, context):
        return self.template.format(**context)

    def formatMultiple(self, contexts):
        html = ''
        for context in contexts:
            html += self.format(context)

        return html



def templatePath(template):
    return f'page/templates/{template}'
