from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
import utility as utl
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session

app = Flask(__name__, static_url_path='/static')
secret_key = 'edutech'
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = secret_key
app.config.from_object(__name__)
Session(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            email = request.form['email']
            Name=request.form['name']
            dataset=request.files['dataset']
            session['email'] = email
            session['Name']=Name
            
            dataset.save(dataset.filename)
            numberofcolumns=request.form['numberofcolumns']
            session['numberofcolumns']=int(numberofcolumns)
            session['filename']=dataset.filename
            return redirect(url_for('dashboard'))
        except:
            flash('Please enter all the details')
            return render_template('index.html')
        
    return render_template('index.html')
@app.route('/dashboard')
def dashboard():
    if session.get('email') is None:
        return redirect(url_for('index'))
    else:
        s=utl.get_dull_students(4,session['filename'])
        below_mean_all_subjects_students=s[0]
        below_mean_all_subjects_students=list(below_mean_all_subjects_students.itertuples(index=False, name=None))
        below_mean_sub_1_students=s[1]
        below_mean_sub_1_students=list(below_mean_sub_1_students.itertuples(index=False, name=None))
        sub_1_mean=s[5]
        below_mean_sub_2_students=s[2]
        below_mean_sub_2_students=list(below_mean_sub_2_students.itertuples(index=False, name=None))
        sub_2_mean=s[6]
        below_mean_sub_3_students=s[3]
        below_mean_sub_3_students=list(below_mean_sub_3_students.itertuples(index=False, name=None))
        sub_3_mean=s[7]
        below_mean_sub_4_students=s[4]
        below_mean_sub_4_students=list(below_mean_sub_4_students.itertuples(index=False, name=None))
        sub_4_mean=s[8]
        return render_template('dashboard.html', email=session['email'],Name=session['Name'],below_mean_all_subjects_students=below_mean_all_subjects_students,sub_1_dataframe=below_mean_sub_1_students,sub_1=sub_1_mean,sub_2_dataframe=below_mean_sub_2_students,sub_2=sub_2_mean,sub_3_dataframe=below_mean_sub_3_students,sub_3=sub_3_mean,sub_4_dataframe=below_mean_sub_4_students,sub_4=sub_4_mean)
            

@app.route('/understand')
def understand():
    return redirect("https://tangy-spell-f83.notion.site/Understand-6b455c282303488e89c624feea46b733",code=302)

@app.route('/Blog')
def blog():
    return render_template("blog.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)