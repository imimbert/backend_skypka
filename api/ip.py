from fastapi import FastAPI, Request
from fastapi import APIRouter
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.header import Header
import datetime

app = FastAPI()

router = APIRouter(
    prefix='/ip',
    tags = ['ip']
)

@router.get("/")
async def get_ip(request: Request):
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    client_ip = request.client.host
    con = smtplib.SMTP_SSL('smtp.qq.com', 465)
    con.login('skypka@qq.com', 'vnmarqwyqqlqdgbi')
    msg = MIMEMultipart()
    subject = Header("new opening", 'utf-8').encode() 
    msg['Subject'] = subject
    msg['From'] = 'skypka@qq.com'
    msg['To'] = "skypka@qq.com"
    content = "ip: "+client_ip+"\ntime: "+formatted_datetime
    html = MIMEText(content, 'html', 'utf-8') 
    msg.attach(html)
    con.sendmail('skypka@qq.com',"skypka@qq.com", msg.as_string()) 
    con.quit()
    return {"code":0,"status":"success"}