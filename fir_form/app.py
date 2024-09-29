from flask import Flask, render_template, request, make_response
import pdfkit

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Check if GET parameters are passed for act and section data
    act1 = request.args.get('act1', '')
    act2 = request.args.get('act2', '')
    act3 = request.args.get('act3', '')
    section1 = request.args.get('section1', '')
    section2 = request.args.get('section2', '')
    section3 = request.args.get('section3', '')

    # Render the form with pre-filled data if available
    return render_template('fir_form.html', act1=act1, act2=act2, act3=act3, 
                                         section1=section1, section2=section2, section3=section3)

@app.route('/submit-fir', methods=['POST'])
def submit_fir():
    # Collect form data
    form_data = {
        'district': request.form.get('district'),
        'ps': request.form.get('ps'),
        'year': request.form.get('year'),
        'firNo': request.form.get('firNo'),
        'date': request.form.get('date'),
        'act1': request.form.get('act1'),
        'section1': request.form.get('section1'),
        'act2': request.form.get('act2'),
        'section2': request.form.get('section2'),
        'act3': request.form.get('act3'),
        'section3': request.form.get('section3'),
        'complainant_name': request.form.get('complainant_name'),
        'father_name': request.form.get('father_name'),
        'dob': request.form.get('dob'),
        'nationality': request.form.get('nationality'),
        'passport_no': request.form.get('passport_no'),
        'occupation': request.form.get('occupation'),
        'address': request.form.get('address')
    }

    # Render the data in an HTML template
    rendered = render_template('fir_pdf_template.html', data=form_data)

    # Convert HTML to PDF
    pdf = pdfkit.from_string(rendered, False)

    # Send the generated PDF back to the user as a response
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=FIR_Form.pdf'

    return response

if __name__ == '__main__':
    app.run(debug=True)
