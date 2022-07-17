from .step import Step


class Preflight(Step):
    def __str__(self):
        return '<class Preflight: This class is prepare everything before run process>'
    
    def process(self, utils, inputs, data):
        return utils.create_dir()
