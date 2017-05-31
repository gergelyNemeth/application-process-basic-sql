from flask import Flask, render_template
import data_manager

app = Flask('application_process')


@app.route('/')
def root():
    return render_template('main.html')


@app.route('/mentors')
def mentors():
    query = data_manager.query()['mentors']
    columns, table = data_manager.query_result(query)
    return render_template('query_result.html', title='Mentors', columns=columns, table=table)


@app.route('/all-school')
def all_school():
    query = data_manager.query()['all_school']
    columns, table = data_manager.query_result(query)
    return render_template('query_result.html', title='All school', columns=columns, table=table)


@app.route('/mentors-by-country')
def mentors_by_country():
    query = data_manager.query()['mentors_by_country']
    columns, table = data_manager.query_result(query)
    return render_template('query_result.html', title='Mentors by country', columns=columns, table=table)


@app.route('/contacts')
def contacts():
    query = data_manager.query()['contacts']
    columns, table = data_manager.query_result(query)
    return render_template('query_result.html', title='Contacts', columns=columns, table=table)


@app.route('/applicants')
def applicants():
    query = data_manager.query()['applicants']
    columns, table = data_manager.query_result(query)
    return render_template('query_result.html', title='Applicants', columns=columns, table=table)


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    query = data_manager.query()['applicants_and_mentors']
    columns, table = data_manager.query_result(query)
    return render_template('query_result.html', title='Applicants and mentors', columns=columns, table=table)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
