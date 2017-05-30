from flask import Flask, render_template
import data_manager

app = Flask('application_process')


@app.route('/')
def root():
    return render_template('main.html')


@app.route('/mentors')
def mentors():
    coloumn_name, table_data = data_manager.query_mentors()
    return render_template('query_result.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
