from flask import Flask, jsonify,render_template, request

app = Flask(__name__, template_folder='templates')


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/appointment')
def appointment():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            mobile = request.form.get('mobile')
            doctor = request.form.get('doctor')
            date = request.form.get('date')
            time = request.form.get('time')
            problem = request.form.get('problem')

            # Debugging logs
            logger.debug(f"Received form data: Name={name}, Email={email}, Mobile={mobile}, Doctor={doctor}, Date={date}, Time={time}, Problem={problem}")

            # Prepare email details
            subject = 'New Appointment Booking'
            body = f'''
            Appointment Details:
            Name: {name}
            Email: {email}
            Mobile: {mobile}
            Doctor: {doctor}
            Date: {date}
            Time: {time}
            Problem: {problem}
            '''

            # Send confirmation email
            if send_email(email, subject, body):
                logger.info(f"Appointment booked successfully for {name} ({email})")
                return jsonify({'message': 'Appointment booked successfully!'})
            else:
                logger.error(f"Error booking appointment for {name} ({email})")
                return jsonify({'message': 'Error booking appointment.'}), 500

        except Exception as e:
            logger.error(f"Exception occurred: {e}")
            return jsonify({'message': 'An error occurred during the booking process.'}), 500

    # If the request method is GET, render the appointment page
    return render_template('appointment.html')

@app.route('/about')
def About():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service')
def service():
    return render_template('service.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)