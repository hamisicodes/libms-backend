
#!/bin/ash

echo $ENVIRONMENT

if [ "$ENVIRONMENT" = "dev" ]; then
    python manage.py makemigrations && python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
else
    echo "Our prod environment"
fi

