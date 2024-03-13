import os
import re

# 正则表达式，用于匹配index.md中的publication字段和cite.bib中的journaltitle字段
regex_pub = re.compile(r'publication: "(.*?)"')
regex_cite = re.compile(r'journaltitle = \{(.+?)\},')
regex_publish_date = re.compile(r'publishDate: \'(.+?)\'')

# 遍历content/publication下的所有子文件夹
for foldername in os.listdir('content/publication'):
    folder_path = os.path.join('content/publication', foldername)
    
    # 确保是文件夹
    if os.path.isdir(folder_path):
        index_md_path = os.path.join(folder_path, 'index.md')
        cite_bib_path = os.path.join(folder_path, 'cite.bib')
        
        # 检查index.md是否存在
        if os.path.exists(index_md_path):
            # 读取index.md内容
            with open(index_md_path, 'r', encoding='utf-8') as file:
                index_md_content = file.read()
            
            # 检查index.md中是否已经有publication字段
            if regex_pub.search(index_md_content):
                continue  # 如果有，跳过该文件夹
            
            # 检查cite.bib是否存在
            if os.path.exists(cite_bib_path):
                # 读取cite.bib内容
                with open(cite_bib_path, 'r', encoding='utf-8') as file:
                    cite_bib_content = file.read()
                
                # 提取期刊名
                match = regex_cite.search(cite_bib_content)
                if match:
                    journal_title = match.group(1)
                    # 构造要插入到index.md的内容
                    insert_text = f'publication: "{journal_title}"\n'
                    
                    # 找到publishDate的位置，并在它前面插入publication字段
                    match_publish_date = regex_publish_date.search(index_md_content)
                    if match_publish_date:
                        publish_date_pos = match_publish_date.start()
                        # 插入文本
                        index_md_content = index_md_content[:publish_date_pos] + insert_text + index_md_content[publish_date_pos:]
                        
                        # 保存修改后的index.md
                        with open(index_md_path, 'w', encoding='utf-8') as file:
                            file.write(index_md_content)
