# {fact rule=cross-site-scripting@v1.0 defects=1}
from flask import app


@app.route('/redirect')
def redirect_url_non_complaint():
    from flask import request, redirect
    endpoint = request.args['url']
    # Noncompliant: redirect to a user-supplied URL without sanitization.
    return redirect(endpoint)
# {/fact}


# {fact rule=cross-site-scripting@v1.0 defects=0}
from flask import app


@app.route('/redirect')
def redirect_url_complaint():
    from flask import request, url_for, redirect
    endpoint = request.args['url']
    # Compliant: user-supplied URL is sanitized before redirecting to it.
    return redirect(url_for(endpoint))
# {/fact}
