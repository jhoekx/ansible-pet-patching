# SPDX-License-Identifier: GPL-3.0-or-later

import json
import subprocess

import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    group_name = None
    results = []
    if 'group-name' in flask.request.form and flask.request.form['group-name'].strip() != '':
        group_name = flask.request.form['group-name']
        results = list_group_updates(group_name)

    return flask.render_template('index.html', group_name=group_name, results=results)


@app.route('/api/list_updates')
def list_updates():
    group = 'all'
    return flask.jsonify(list_group_updates(group))


def list_group_updates(group_name):
    process = subprocess.run(
        ['ansible', group_name, '-m', 'list_updates'], capture_output=True)
    ansible_run = json.loads(process.stdout)
    ansible_task = ansible_run['plays'][0]['tasks'][0]

    results = []
    for hostname, result in ansible_task['hosts'].items():
        if 'unreachable' in result and result['unreachable'] == True:
            results.append({
                'hostname': hostname,
                'installed': [],
                'updates': [],
                'msg': result['msg']
            })
            continue

        results.append({
            'hostname': hostname,
            'installed': result['installed'],
            'updates': result['updates']
        })
    return results
