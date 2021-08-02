from .utils import *


class ExtractCSSClasses:
    def __init__(self, ParentClass):
        self.sub_classes = filter_builtins(ParentClass)
        # A list of all the Python classes being used to generate CSS
        self.sub_class_list = [c for c in self.sub_classes]

        self.final_class_list = []
        for sub_class_name in self.sub_class_list:
            css_class = getattr(ParentClass, sub_class_name)
            self.final_class_list.append(css_class)
        self.extract()

    def extract(self):
        return self.final_class_list


class GenerateCSSClass:
    def __init__(self, MainCSSClass, output_file):
        self.class_list = ExtractCSSClasses(MainCSSClass).extract()
        self.output_file = output_file
        self.compiled_css = ""  # Compiled CSS
        self.compile()

    def compile(self):
        for _class in self.class_list:
            css_class_name = cleanse_css_line(_class.__name__).lower()
            output_class = f".{css_class_name} {{\n"

            css_properties = filter_builtins(_class)
            for css_prop in css_properties:
                css_value = getattr(_class, css_prop)
                output_class += f"\t{css_prop}: {css_value};\n"
            output_class += "}\n\n"
            self.compiled_css += output_class

        write(self.output_file, f"{CSS_HEADER}\n\n{self.compiled_css}")
