from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
P=Path('.')
def font(size,bold=True):
 for f in (['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'] if bold else ['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']):
  try:return ImageFont.truetype(f,size)
  except OSError:pass
 return ImageFont.load_default()
def bg(size,dark=True):
 im=Image.new('RGBA',(size,size),(9,14,27,255) if dark else (237,245,253,255))
 d=ImageDraw.Draw(im)
 for i in range(0,size,16):
  d.line((0,i,size,i),fill=(40,65,88,55) if dark else (190,213,225,50),width=1)
 return im
def mark(im,scale=1):
 d=ImageDraw.Draw(im);w,h=im.size;cx=w//2;cy=h//2
 r=int(min(w,h)*.26*scale);stroke=max(10,int(r*.16))
 d.rounded_rectangle((cx-r,cy-r,cx+r,cy+r),radius=int(r*.35),outline=(91,238,214,255),width=stroke)
 d.line([(cx-r//2,cy+r//2),(cx-r//2,cy-r//2),(cx+r//2,cy+r//2),(cx+r//2,cy-r//2)],fill=(237,247,255,255),width=stroke,joint='curve')
def save_icon():
 im=bg(1024);mark(im);im.convert('RGB').save('icon-only.png')
 im.save('icon-background.png')
 fg=Image.new('RGBA',(1024,1024),(0,0,0,0));mark(fg);fg.save('icon-foreground.png')
def splash(dark,name):
 w=2732;im=bg(w,dark);mark(im,.55);d=ImageDraw.Draw(im)
 title='NEXUS';f=font(180);bb=d.textbbox((0,0),title,font=f);d.text(((w-(bb[2]-bb[0]))/2,w*.70),title,font=f,fill=(107,232,212,255) if dark else (14,97,112,255))
 sub='YOUR OFFLINE COMMAND CENTER';f=font(55,False);bb=d.textbbox((0,0),sub,font=f);d.text(((w-(bb[2]-bb[0]))/2,w*.80),sub,font=f,fill=(180,196,216,255) if dark else (50,80,103,255))
 im.convert('RGB').save(name)
save_icon();splash(False,'splash.png');splash(True,'splash-dark.png')
