import os
import re

txt_file = "input0.txt"
pdf_dir = "."  # 当前目录

with open(txt_file, "r", encoding="utf-8") as f:
    for line in f:
        # 匹配 arXiv 号和标题
        m = re.search(r"\[paper\]\(https://arxiv\.org/pdf/(\d+\.\d+)\)", line)
        t = re.search(r"\[\d+\]\s*(.*?)\s*\[\[paper\]", line)
        if m and t:
            arxiv_id = m.group(1)
            title = t.group(1).replace("/", "-")  # 防止标题中有斜杠
            # 查找所有以 arxiv_id 开头的 pdf 文件
            for fname in os.listdir(pdf_dir):
                if fname.startswith(arxiv_id) and fname.endswith(".pdf"):
                    new_name = f"{title}.pdf"
                    os.rename(os.path.join(pdf_dir, fname), os.path.join(pdf_dir, new_name))
                    print(f"Renamed: {fname} -> {new_name}")