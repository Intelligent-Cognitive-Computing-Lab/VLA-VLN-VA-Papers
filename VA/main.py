import re

def extract_arxiv_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # 匹配 https://arxiv.org/pdf/xxxx.xxxxx 或 https://arxiv.org/pdf/xxxx.xxxxx.pdf
    pattern = r'https://arxiv\.org/pdf/(\d{4}\.\d{5}(v\d+)?)(?:\.pdf)?'
    matches = re.findall(pattern, content)
    links = [f'https://arxiv.org/pdf/{arxiv_id}' for arxiv_id, *_ in matches]
    return links

if __name__ == '__main__':
    input_file = 'input.txt'
    output_file = 'output.txt'
    links = extract_arxiv_links(input_file)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(links))