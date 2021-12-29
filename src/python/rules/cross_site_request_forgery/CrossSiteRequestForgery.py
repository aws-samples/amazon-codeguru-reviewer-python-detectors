# {fact rule=cross-site-request-forgery@v1.0 defects=1}
def csrf_protection_non_compliant():
    from flask import Flask
    app = Flask(__name__)
    # Noncompliant: disables CSRF protection.
    app.config['WTF_CSRF_ENABLED'] = False
# {/fact}


# {fact rule=cross-site-request-forgery@v1.0 defects=0}
def csrf_protection_compliant():
    from flask_wtf.csrf import CsrfProtect
    from flask import Flask
    csrf = CsrfProtect()
    app = Flask(__name__)
    # Compliant: enables CSRF protection.
    csrf.init_app(app)
# {/fact}
