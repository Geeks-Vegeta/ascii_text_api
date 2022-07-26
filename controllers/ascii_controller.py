from pyfiglet import figlet_format
from flask import send_file
import random
import io
import base64
import os

def create_art(query, fonts):

    rannum = random.randint(1, 1111)
    filename = f"asciiart{rannum}.txt"

    try:
        art=figlet_format(text=query,font=fonts)
        with open(filename, "w") as f:
            f.write(art)
        print(art)
        return_data = io.BytesIO()
        with open(filename, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)  
        os.remove(filename)
        return send_file(return_data,as_attachment=True,mimetype='text/plain',
                    attachment_filename=f'ascii_art{rannum}.txt')

    except Exception as e:
        print(e)

    