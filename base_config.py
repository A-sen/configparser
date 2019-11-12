# -*- coding: utf-8 -*-

"""
@author: Arsen

@contact: E-mall:949616581@qq.com

@Created on: 2019/9/27 0027 下午 4:56
"""
import os
import configparser

'''
    参数说明：
    flag：文件读写模式[r:读； w:写]
    filepath：文件完整路径
    sections：节点
    options：选项
    charset：字符集
    **items：写入值
'''


class GlobalConfig(object):
    def __init__(self, filepath=None, sections=None, options=None, charset='utf-8'):
        self.filepath = filepath
        self.sections = sections
        self.options = options
        self.charset = charset

    def global_config_read(self):
        config = configparser.ConfigParser()
        # 读取配置文件
        if not os.path.exists(self.filepath):
            print("配置文件不存在，请核对：" + self.filepath)
            return False
        config.read(self.filepath, encoding=self.charset)
        r_items = {}
        if not self.sections or not self.options:
            print("核对参数sections和options,当前：" + 'sections:' + self.sections + '  options:' + self.options)
            return False
        for section in self.sections:
            for option in self.options:
                if not config.has_option(section, option):
                    continue
                r_items[option] = config.get(section, option)
        return r_items

    # 写配置文件
    def global_config_write(self, section, **items):
        config = configparser.ConfigParser()
        config.read(self.filepath, encoding=self.charset)
        '''
            关于open()的mode参数：
            'r'：读
            'w'：写
            'a'：追加
            'r+' == r+w（可读可写，文件若不存在就报错(IOError)）
            'w+' == w+r（可读可写，文件若不存在就创建）
            'a+' ==a+r（可追加可写，文件若不存在就创建）
            对应的，如果是二进制文件，就都加一个b就好啦：
            'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+'

        '''
        with open(self.filepath, mode='w', encoding=self.charset) as configfile:
            section = section.strip()
            if config.has_section(section):
                for key in items:
                    item_ = items[key]
                    if item_:
                        config.set(section, key, item_)
            else:
                config.add_section(section)
                for key, value in items.items():
                    config.set(section, key, value)
            config.write(configfile)


def main():
    sections = ['PATH', 'LABELS', 'TOKEN_DIC', 'JSON2MODEL', '1111']
    options = ['original', 'labels', '1112']
    config = GlobalConfig(filepath='base-config.ini', sections=sections, options=options, charset='utf-8')
    r_item = config.global_config_read()
    print(r_item)
    _section = 'PATH'
    _item = {'original': '5454555454545', 'labels': '2200000000000002', 'wqs': '12121212112'}
    config.global_config_write(_section, **_item)


if __name__ == '__main__':
    main()
