## Setup

1. Install the required packages:

```bash
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```

2. Set up ngrok:

```bash
$ ngrok authtoken <your_authtoken>
```

3. Run the prediction API:

```bash
$ python main.py
```

## Usage

To use the prediction API, send a POST request to `/predict` with an image file. The API will return the predicted disease label.

ลบ cash gitignore

```bash
$ git rm --cached models\resnet50_finetuned_model.h5
$ git rm --cached data -r
```

หรือ

```bash
git rm -r --cached .
git add .
git commit -am 'git cache cleared'
git push
```

การย้อนกลับการกระทำครั้งล่าสุด

```bash
git reset HEAD^ --hard
```

---

# Virtual Environment

```bash
python -m venv venv  # สร้าง virtual environment
or 
python3 -m venv venv
```

## ใช้งาน virtual environment
```bash
source venv/bin/activate  # สำหรับ macOS/Linux
venv\Scripts\activate  # สำหรับ Windows
```

## Deactivate Virtual Environment (ออกจาก venv)
การออกจาก virtual environment (venv)
```bash
deactivate
```

- เช็ค Python ว่ากำลังใช้จาก Virtual Environment หรือไม่

```bash
python -c "import sys; print(sys.prefix)"
```

- ถ้า Virtual Environment ถูกเปิดอยู่ มันควรจะแสดง path ของ env เช่น

```bash
C:\Users\YourUser\YourProject\env
```

---

## Execution Policy ของ PowerShell ที่ไม่อนุญาตให้เรียกใช้สคริปต์ (.ps1)

- เปิด PowerShell ด้วยสิทธิ์ Admin
- ตรวจสอบ Execution Policy พิมพ์คำสั่งนี้เพื่อตรวจสอบค่า Policy ปัจจุบัน

```bash
Get-ExecutionPolicy
```

- เปลี่ยน Execution Policy ใช้คำสั่งนี้เพื่ออนุญาตให้รันสคริปต์:

```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

- ลอง Activate Virtual Environment อีกครั้ง

```bash
<ชื่อ>\Scripts\Activate
```

- หรือหากใช้ WSL หรือ macOS/Linux:

```bash
source env/bin/activate
```

## ยกเลิก หรือ ตั้งค่า Execution Policy กลับเป็นค่าเริ่มต้น

- ตั้งค่าเป็นค่าเริ่มต้นของ Windows

```bash
Set-ExecutionPolicy Restricted -Scope CurrentUser
```

---

# Run project

```bash
uvicorn main:app --reload
```

ถ้าเชื่อมต่อ git ด้วย ssh ไม่ได้อาจมาจาก
การปรับเปลี่ยนไฟร์วอลล์เนื่องจากคุณอยู่บนเครือข่าย ในกรณีนี้พวกเขาอาจบล็อกพอร์ตบางพอร์ตโดยตั้งใจ
พื่อตรวจสอบอีกครั้งว่านี่คือสาเหตุหรือไม่ ให้รัน:

```bash
ssh -T git@github.com
```

ให้ใช้httpโปรโตคอลแทน ssh เปลี่ยน URL ของคุณในไฟล์ config เป็นhttp

```bash
git config --local -e
```

หรือเปิดไฟล์ `.git\config`
และเปลี่ยน:

```bash
 url = git@github.com:username/repo.git
```

เป็น

```bash
url = https://github.com/username/repo.git
```

# ทดสอบ

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/status' \
  -H 'accept: application/json'
```

```bash
curl --location 'http://127.0.0.1:8000/predict' \
--form 'file=@"/path/to/file"'
```

```
python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl
```


## เช็กว่า Python 3.11 ถูกติดตั้งที่ไหน
```
which python3.11
```

## ตั้ง alias ให้ชี้ไปที่ Python 3.11 ที่ถูกต้อง
```
alias python=/opt/homebrew/bin/python3.11
```

## ทดสอบ
```
python --version
```

## run
```
uvicorn main:app --reload
```