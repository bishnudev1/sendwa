from flask import Flask, render_template, request, redirect
import pywhatkit

app = Flask(__name__)


@app.route('/SendWA', methods=['GET', 'POST'])
def sendWA():
    status = 'Send a message now😛'
    if request.method == 'POST':
        try:
            num = request.form['num']
            msg = request.form['msg']
            hour = request.form['hour']
            minutes = request.form['minute']
            wait_time = request.form['second']
            status = 'Message has been sent😺'
            pywhatkit.sendwhatmsg(f"+91{num}", f"{msg}", int(
                hour), int(minutes), int(wait_time), True, 2)
            redirect('/SendWA')
        except Exception as e:
            print(e)
    return render_template('index.html', status=status,error = e)


if __name__ == "__main__":
    app.run(debug=True)
