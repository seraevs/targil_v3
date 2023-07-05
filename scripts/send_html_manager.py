# =====================================
# ============= The python ============
# ======= Code Jenkins Report =========
# =====================================
import codecs
import sys
from mails import send_mail
from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates/"))
path_to_html = environment.get_template("index.html")

mail_subject = "CI/CD FAILED!!! Customer-App Project Reports."
mail_from = "serakuz51@gmail.com"
mail_to = "serakuz51@gmail.com"
mail_cc = "serakuz51@gmail.com"
ip_smtp = '10.0.0.1'
port_smtp = 587
########################################################################################################
ca_row_style_red = "background-color:red;"
ca_row_style_black = "background-color:#728FCE;"
########################################################################################################
## Stages color variables
a1 = ""
a2 = ""
a3 = ""
a4 = ""
a5 = ""
a6 = ""
a7 = ""
a8 = ""
########################################################################################################
# HTML Message Part
f = codecs.open("/jenkins/workspace/targil_v3Prj/targil_v3/scripts/templates/index.html", 'r')
########################################################################################################
_color = "red"
"color:black; background-color:red;"
# leo_row_style = "bgcolor:#728FCE; color:red"
_style = "background-color:red;"
status_title = "Project build failed"
########################################################################################################
message = "Messagd"
########################################################################################################
print('============= test =================')
for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])
print('============= test =================')
########################################################################################################
print(sys.argv[1])
argument = sys.argv[1]
if "Clean_Pre_Archive	" == argument:
    a1 = _style

if "Git_Clone" == argument:
    a2 = _style

if "Docker_Build" == argument:
    a3 = _style

if "Docker_Run" == argument:
    a4 = _style

if "Docker_Tar" == argument:
    a5 = _style
  
 if "Artifactory " == argument:
    a6 = _style 

if "Finish" == argument:
    a7 = _style

if "Sending_Mail" == argument:
    a8 = _style
########################################################################################################
# leo_status_title = "Leo project build finished successfully"
html = f.read().format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7, _color=_color, status_title=status_title)
########################################################################################################
dir_path=""
files=""
filename_report=""
# Create MIMEMultipart object
try:
    send_mail(filename_report,
              mail_subject,
              mail_from,
              mail_to,
              mail_cc,
              html,
              files,
              dir_path,
              ip_smtp,
              port_smtp)

except Exception as e:
    print(e)
