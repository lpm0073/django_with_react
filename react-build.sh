#!/usr/bin/env bash
#-------------------------------------------------------
# 1. execute react-scripts build
# 
# 2. run Django manage.py collectstatic in order to 
# copy React build files to the staticfiles serving area.
#-------------------------------------------------------
cd django_with_react/djangoapps/frontend/
yarn run build
cd ../../..
docker-compose -f ./local.yml run --rm django python manage.py collectstatic
