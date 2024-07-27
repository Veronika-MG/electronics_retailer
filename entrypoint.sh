#!/bin/bash

set -e
python electronics_retailer/manage.py migrate
if python electronics_retailer/manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.exists())" | grep -q "False"; then
    python electronics_retailer/manage.py loaddata electronics_retailer/fixtures/data.json
fi
exec "$@"