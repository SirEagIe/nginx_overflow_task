#!/bin/bash
/etc/init.d/nginx restart

su app -c "python3 -u app.py"
