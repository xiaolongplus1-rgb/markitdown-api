from fastapi import FastAPI, UploadFile, File
from markitdown import MarkItDown
import os

app = FastAPI()
md = MarkItDown()

@app.post("/parse")
async def parse_doc(data: UploadFile = File(...)):
    # 这里的 data 已经改好，对应扣子插件里的 data 参数
    temp_path = f"temp_{data.filename}"
    with open(temp_path, "wb") as f:
        f.write(await data.read())
    
    # 使用 MarkItDown 进行文档解析
    result = md.convert(temp_path)
    
    # 清理临时文件
    os.remove(temp_path)
    
    # 返回 Markdown 格式的文本内容
    return {"markdown": result.text_content}
