U
    �{_�  �                   @   s   d dl Z G dd� d�ZdS )�    Nc                   @   s(   e Zd ZdZdd� Zdd� Zdd� ZdS )	�chatBotzinput chat e.g chatbot("Hi")c              	   C   s�   |� � �� | _dddg| _dddg| _ddg| _d	d
dd
dddddg	| _dddddg| _ddddddddg| _dddg| _	d d!dd"g| _
d#d$g| _d d%d&d'd(dg| _d)d*g| _d+d,g| _d-d.g| _d/d0d1g| _d2d3d4g| _d S )5NZakuZsayangZkamuZsamez:)zkamu bilang apaZhiuZtomat�hiZhaiZhello�pZbroZhaloZhalloZheloZiyazada apa ganzya hallozada apaan ganZYaZdimana�rumahZtempatZtinggalZdaerahZdiZmanaz
Jawa Baratzjawa Tengahz
Jawa TimurZsiapa�namaZnamanyaznama saya chappiez1nama saya chappie atau bisa di sebut Bot whatsapp�authorZpembuatZpenciptaZmenciptakanZNtahzsaya Tidak Tahuzassalamu'alaikum�asalamualaikumzwa'alaikumsalamzWa'alaikumsalamZmakananZfavoritZkesukaanzNasi GorengzTelur Ceplokz
Mie Goreng)�lower�split�req�list_ask�	balas_ask�list_odading�
list_intro�balas_intro�
list_rumah�balas_rumah�	list_nama�
balas_nama�list_author�balas_author�
list_salam�balas_salam�list_fav_makanan�balas_fav_makanan)�selfr   � r   �+/home/krypton-byte/N-BOT/pustaka/chatbot.py�__init__   s     




zchatBot.__init__c                 C   s�   t t| j�t| j�@ �| _t t| j�t| j�@ �| _t t| j�t| j�@ �| _t t| j	�t| j�@ �| _
t t| j�t| j�@ �| _t t| j�t| j�@ �| _t t| j�t| j�@ �| _t t| j�t| j�@ �| _| j| j| j| j
| j| j| j| jg| _d S )N)�len�setr   r   r   r   r   r   r   r   �salamr   �intror   �fav_makananr   �askr   �odading�list)r   r   r   r   �max_   s    zchatBot.max_c                 C   s�   t | j�}t| j� d| jkrDtddg�t| j�@ rDt�dddg�S |dkrPdS | j|krft�| j�S | j	|kr|t�| j
�S | j|kr�t�| j�S | j|kr�t�| j�S | j|kr�t�| j�S | j|kr�t�| j�S | j|kr�t�| j�S | j|k� r�d	S d S )
N�botZgoblokZtololzyg main bot gk ada akhlakznama nya juga botz@aku ini bukan bot sepeti ML (machine learning) yg bisa di ajarinr   Fz
Goblok !!!)�maxr&   �printr   r    �random�choicer   r   r   r   r   r   r!   r   r#   r   r"   r   r$   r   r%   )r   Zmaksr   r   r   �balas   s,    

 






zchatBot.balasN)�__name__�
__module__�__qualname__�__doc__r   r'   r-   r   r   r   r   r      s   
r   )r+   r   r   r   r   r   �<module>   s   