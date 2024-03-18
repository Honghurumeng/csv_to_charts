import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import tkinter
import tkinter.filedialog
from tkinter import ttk

window = tkinter.Tk()
window.title('Csv to Charts Converter')
# window.geometry('770x650')
window.resizable(False, False)


folderPath = tkinter.StringVar()
folderPathinfo = tkinter.Entry(window, width=40, textvariable=folderPath)
folderPathinfo.grid(column=1, row=3, sticky='we')

def choosefolderPath():
    global folderPath
    folderPath = tkinter.filedialog.askdirectory(initialdir=os.path.dirname(__file__))
    # 把文件路径显示在输入框中
    folderPathinfo.delete(0, tkinter.END)
    folderPathinfo.insert(0, folderPath)

choosefolderPathBtn = tkinter.Button(window, text="选择CSV文件夹", command=choosefolderPath)
choosefolderPathBtn.grid(column=0, row=3, sticky='w')


def createCharts():
    try:
        fig = go.Figure()

        # 遍历文件夹中的所有 CSV 文件
        for filename in os.listdir(folderPath):
            if filename.endswith(".csv"):
                # 读取 CSV 文件
                df = pd.read_csv(os.path.join(folderPath, filename))
                # print(df)   
                # 计算每行的正数之和
                df_sum = df.iloc[1:, 3:][df.iloc[1:, 3:] > 0].sum(axis=1)

                # 添加到折线图
                fig.add_trace(go.Scatter(y=df_sum, mode='lines', name=filename))

        # 显示图形
        fig.show()
    except Exception as e:
        print(f"An error occurred: {e}")

createBtn = tkinter.Button(window, text="生成曲线", command=createCharts)
createBtn.grid(column=0, row=4, sticky='w')



window.mainloop()