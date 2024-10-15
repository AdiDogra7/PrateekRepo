from django.http import HttpResponse

def hello_view(request):
    # Use session to count the number of visits
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits

    # Create the response object
    response = HttpResponse(f"""
        <html>
            <body>
                <h1>Hello, World!</h1>
                <p>This is visit number {num_visits}.</p>
                <p>Unique code: 1afd756e</p>
            </body>
        </html>
    """)

    # Set the cookie
    response.set_cookie('dj4e_cookie', '1afd756e', max_age=1000)

    return response
