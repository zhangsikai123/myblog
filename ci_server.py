#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sikai.zhang
# @Time    : 11/2/19 10:37 PM
import os
import subprocess
from flask import Flask

app = Flask('Ci')


@app.route('/whosdaddy', methods=['POST'])
def after_git_push():
    command_line = './restart.sh >> ci.log'
    args = command_line.split(' ')
    subprocess.Popen(args)
    return 'OK'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8081)),
            debug=app.config['DEBUG'])
