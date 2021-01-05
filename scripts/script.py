from weasyprint import HTML

HTML(filename="relatorio_cof.html", base_url= "").write_pdf("teste5_pdf.pdf")


"""
sudo apt install virtualenv
[sudo] password for lse:     ]
Lendo listas de pacotes... Pronto
Construindo árvore de dependências       
Lendo informação de estado... Pronto
The following additional packages will be installed:
  python-pip-whl python3-virtualenv
Os NOVOS pacotes a seguir serão instalados:
  python-pip-whl python3-virtualenv virtualenv
0 pacotes atualizados, 3 pacotes novos instalados, 0 a serem removidos e 0 não atualizados.
É preciso baixar 1.701 kB de arquivos.
Depois desta operação, 2.029 kB adicionais de espaço em disco serão usados.
Você quer continuar? [S/n] 
Obter:1 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 python-pip-whl all 9.0.1-2.3~ubuntu1.18.04.4 [1.653 kB]
Obter:2 http://archive.ubuntu.com/ubuntu bionic/universe amd64 python3-virtualenv all 15.1.0+ds-1.1 [43,4 kB]
Obter:3 http://archive.ubuntu.com/ubuntu bionic/universe amd64 virtualenv all 15.1.0+ds-1.1 [4.476 B]
Baixados 1.701 kB em 3s (523 kB/s)     
debconf: incapaz de inicializar interface: Dialog
debconf: (A interface dialog requer uma tela de pelo menos 13 linhas de altura e 31 colunas de largura.)
debconf: tentando com interface: Readline
A seleccionar pacote anteriormente não seleccionado python-pip-whl.
(Lendo banco de dados ... 303629 ficheiros e directórios actualmente instalados.)
A preparar para desempacotar .../python-pip-whl_9.0.1-2.3~ubuntu1.18.04.4_all.deb ...
A descompactar python-pip-whl (9.0.1-2.3~ubuntu1.18.04.4) ...
A seleccionar pacote anteriormente não seleccionado python3-virtualenv.
A preparar para desempacotar .../python3-virtualenv_15.1.0+ds-1.1_all.deb ...
A descompactar python3-virtualenv (15.1.0+ds-1.1) ...
A seleccionar pacote anteriormente não seleccionado virtualenv.
A preparar para desempacotar .../virtualenv_15.1.0+ds-1.1_all.deb ...
A descompactar virtualenv (15.1.0+ds-1.1) ...
Configurando python-pip-whl (9.0.1-2.3~ubuntu1.18.04.4) ...
Configurando python3-virtualenv (15.1.0+ds-1.1) ...
Configurando virtualenv (15.1.0+ds-1.1) ...
A processar 'triggers' para man-db (2.8.3-2ubuntu0.1) ...

lse@lse-K46CA:~/Documentos/html$ virtualenv venv --python=python3

Running virtualenv with interpreter /home/lse/anaconda3/envs/rstudio-vitor/bin/python3
Using base prefix '/home/lse/anaconda3/envs/rstudio-vitor'
/usr/lib/python3/dist-packages/virtualenv.py:1086: DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
  import imp
New python executable in /home/lse/Documentos/html/venv/bin/python3
Also creating executable in /home/lse/Documentos/html/venv/bin/python
Installing setuptools, pkg_resources, pip, wheel...done.

lse@lse-K46CA:~/Documentos/html$ rm /home/lse/Documentos/html/venv/bin/python
lse@lse-K46CA:~/Documentos/html$ source venv/bin/activate

(venv) lse@lse-K46CA:~/Documentos/html$ pip3 install weasyprint
Collecting weasyprint
  Using cached WeasyPrint-52.2-py3-none-any.whl (363 kB)
Requirement already satisfied: setuptools>=39.2.0 in ./venv/lib/python3.8/site-packages (from weasyprint) (51.0.0)
Collecting cairocffi>=0.9.0
  Using cached cairocffi-1.2.0-py3-none-any.whl
Collecting CairoSVG>=2.4.0
  Using cached CairoSVG-2.5.0-py3-none-any.whl (45 kB)
Collecting cffi>=0.6
  Downloading cffi-1.14.4-cp38-cp38-manylinux1_x86_64.whl (411 kB)
     |████████████████████████████████| 411 kB 326 kB/s 
Collecting cssselect2>=0.1
  Using cached cssselect2-0.4.1-py3-none-any.whl (13 kB)
Collecting defusedxml
  Downloading defusedxml-0.6.0-py2.py3-none-any.whl (23 kB)
Collecting html5lib>=0.999999999
  Using cached html5lib-1.1-py2.py3-none-any.whl (112 kB)
Collecting Pillow>=4.0.0
  Using cached Pillow-8.0.1-cp38-cp38-manylinux1_x86_64.whl (2.2 MB)
Collecting pycparser
  Downloading pycparser-2.20-py2.py3-none-any.whl (112 kB)
     |████████████████████████████████| 112 kB 6.5 MB/s 
Collecting Pyphen>=0.9.1
  Using cached Pyphen-0.10.0-py3-none-any.whl (1.9 MB)
Collecting six>=1.9
  Downloading six-1.15.0-py2.py3-none-any.whl (10 kB)
Collecting tinycss2>=1.0.0
  Using cached tinycss2-1.1.0-py3-none-any.whl (21 kB)
Collecting webencodings
  Downloading webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Installing collected packages: webencodings, pycparser, tinycss2, cffi, six, Pillow, defusedxml, cssselect2, cairocffi, Pyphen, html5lib, CairoSVG, weasyprint
Successfully installed CairoSVG-2.5.0 Pillow-8.0.1 Pyphen-0.10.0 cairocffi-1.2.0 cffi-1.14.4 cssselect2-0.4.1 defusedxml-0.6.0 html5lib-1.1 pycparser-2.20 six-1.15.0 tinycss2-1.1.0 weasyprint-52.2 webencodings-0.5.1
(venv) lse@lse-K46CA:~/Documentos/html$ python3 script.py
(venv) lse@lse-K46CA:~/Documentos/html$ 
nodemon script.py  --watch *.html
"""