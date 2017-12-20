# -*- coding:gb2312 -*-
import requests
import xml.etree.ElementTree as ET
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def __init__(self, provinces):
        self.provinces = provinces



    # �����ǩ��ʼ

    def start_element(self, name, attrs):
        if name != 'map':
            name = attrs['title']
            number = attrs['href']
            self.provinces.append((name, number))

    # �����ǩ����

    def end_element(self, name):
        pass

    # �ı�����
    def char_data(self, text):
        pass


def get_province_entry(url):
    # ��ȡ�ı�������utf-8�ֽ�
    content = requests.get(url).content.decode('gb2312')
    
    # ȷ��Ҫ�����ַ����Ŀ�ʼ����λ�ã�������Ƭ��ȡ���ݡ�
    start =  content.find('<map name=\"map_86\" id=\"map_86\">')
                            
    end =  content.find('</map>')

    # xml �ļ���һ���ı� 
    content =  content[start: end + len('</map>')].strip()
    
    
    provinces = []
    
    # ����Sax������
    handler = DefaultSaxHandler(provinces)
    
    # ��ʼ��������
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
            
    # ��������
    parser.Parse(content)
    # ����ֵ�Ϊÿһҳ����ڴ���
    return provinces
    

provinces =get_province_entry('http://www.ip138.com/post')
print(provinces)


    
    


    
    
