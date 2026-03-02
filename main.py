from fastapi import FastAPI, UploadFile, File
from markitdown import MarkItDown
import os

app = FastAPI()
md = MarkItDown()

@app.post("/parse")
async def parse_doc(data: UploadFile = File(...)):
    # 1. 这里的 data 对应扣子插件里的 data 参数名
    temp_path = f"temp_{data.filename}"
    with open(temp_path, "wb") as f:
        # 2. 这里也要改成 data.read()
        f.write(await data.read())
    
    # 3. 转码
    result = md.convert(temp_path)
    
    # 4. 清理
    os.remove(temp_path)
    
    return {"markdown": result.text_content}
