# element_loader.py
import yaml


class ElementLoader:
    def __init__(self):
        with open(r'D:\shixunyi\atee\yongli\data\ui_map.yaml', 'r', encoding='utf-8') as f:
            self.ui_map = yaml.safe_load(f)

    def get_locator(self, page_name, element_name):
        """快速获取定位器"""
        element = self.ui_map[page_name][element_name]
        return (element['locator_type'], element['locator_value'])