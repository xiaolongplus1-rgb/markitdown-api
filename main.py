from fastapi import FastAPI, UploadFile, File
from markitdown import MarkItDown
import os

app = FastAPI()
md = MarkItDown()

@app.post("/parse")
async def parse_doc(file: UploadFile = File(...)):
    # 临时存储上传文件
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())
    
    # 转码
    result = md.convert(temp_path)
    
    # 清理
    os.remove(temp_path)
    
    return {"markdown": result.text_content}
