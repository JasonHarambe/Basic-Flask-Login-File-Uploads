from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.utils import secure_filename
import os

verify = Blueprint('verify', __name__)

uploads_dir = 'uploads'
os.makedirs(uploads_dir, exist_ok=True)

@verify.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join(uploads_dir, filename))
      flash('Uploaded Successfully')
      return redirect(url_for('main.profile'))
