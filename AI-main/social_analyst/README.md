## คำสั่ง git
```
git add <folder_path>

git commit -m "Your commit message"
```

### คำสั่งดู git ที่ add
```
git status
```
คำอธิบายผลลัพธ์:

Changes to be committed: ส่วนนี้แสดงไฟล์ที่ถูก add แล้ว 
(staged) และจะถูก commit ในครั้งต่อไป
Changes not staged for commit: ส่วนนี้แสดงไฟล์ที่มีการเปลี่ยนแปลง แต่ยังไม่ได้ถูก add
Untracked files: ส่วนนี้แสดงไฟล์ใหม่ที่ Git ยังไม่รู้จัก

คำสั่งอื่น ๆ ที่เกี่ยวข้อง:

git diff --cached หรือ git diff --staged: คำสั่งนี้แสดงความแตกต่างระหว่างไฟล์ที่ถูก staged กับเวอร์ชันล่าสุดใน repository (HEAD)
git diff: คำสั่งนี้แสดงความแตกต่างระหว่างไฟล์ที่ถูก modified กับเวอร์ชันล่าสุดใน repository (HEAD)

---

### คำสั่งยกเลิก add
```
git restore --staged <file>
```
---

## สร้าง Python Virtual Environment
```
python3 -m venv env
```

## Activate venv
```
source env/bin/activate 
```