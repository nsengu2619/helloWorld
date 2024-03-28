from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Neena Sengupta! I am adding my first code change'
@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')
@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/about-css')
def about_css():  # put application's code here
    return render_template('about-css.html')

@app.route('/favorite-course')
def favorite_course():  # put application's code here
    course = request.args.get('course')
    course_number = request.args.get('course_number')

    return render_template('favorite-course.html', course=course, course_number=course_number)

@app.route('/test')
def test():  # put application's code here
    return render_template('test.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():  # put application's code here
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')
@app.route('/base')
def base():
    return render_template('base.html')
if __name__ == '__main__':
    app.run()
