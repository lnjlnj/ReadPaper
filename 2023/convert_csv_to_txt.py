import pandas as pd
import os

df = pd.read_csv('csv/cvpr2023_arxiv.csv')
save_path = 'txt/cvpr2023_arxiv.txt'
for index, rows in df.iterrows():
    title = f'{index+1}      {rows["title"]}'
    abstract = f'{rows["abstract"]}'
    content = f'{rows["content"]}'

    filename = save_path
    if os.path.exists(filename) is False:
        with open(filename, "w") as f:
            f.write(f"{'='*73}\n")
            f.write(f"{title:^50}\n")
            f.write(f"{'='*73}\n\n")
            f.write(abstract + "\n")
            f.write(f"{'-'*73}\n\n")
            f.write(f'{content}\n\n\n\n')
            print(f"\n已将打印输出保存到{filename}文件中。")
    else:
        with open(filename, "a") as f:
            f.write(f"{'='*73}\n")
            f.write(f"{title:^50}\n")
            f.write(f"{'='*73}\n\n")
            f.write(abstract + "\n")
            f.write(f"{'-'*73}\n\n")
            f.write(f'{content}\n\n\n\n')
            print(f"\n已将打印输出保存到{filename}文件中。")


