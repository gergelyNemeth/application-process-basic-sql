from flask import Flask, render_template
import data_manager

app = Flask('application_process')


@app.route('/')
def root():
    return render_template('main.html')


@app.route('/mentors')
def mentors():
    columns, table = data_manager.query_mentors()
    return render_template('query_result.html', title='Mentors', columns=columns, table=table)


@app.route('/all-school')
def all_school():
    columns, table = data_manager.query_all_school()
    return render_template('query_result.html', title='All school', columns=columns, table=table)


@app.route('/mentors-by-country')
def mentors_by_country():
    columns, table = data_manager.query_mentors_by_country()
    return render_template('query_result.html', title='Mentors by country', columns=columns, table=table)


@app.route('/contacts')
def contacts():
    columns, table = data_manager.query_contacts()
    return render_template('query_result.html', title='Contacts', columns=columns, table=table)


@app.route('/applicants')
def applicants():
    columns, table = data_manager.query_applicants()
    return render_template('query_result.html', title='Applicants', columns=columns, table=table)


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    columns, table = data_manager.query_applicants_and_mentors()
    return render_template('query_result.html', title='Applicants and mentors', columns=columns, table=table)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
