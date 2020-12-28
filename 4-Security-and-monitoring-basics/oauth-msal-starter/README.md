# OAuth2 with MSAL

This exercise will help you get familiar with integrating the Microsoft Authentication Library,
or `msal`, into an application. Azure Active Directory is Microsoft’s solution for single sign-on (SSO)
and multi-factor authentication (MFA). We'll be using it in combination with the Microsoft Authentication Library (MSAL)
to use "Sign in with Microsoft" buttons in an app, although it can be used more broadly for identity management purposes
within an organization.

## App registration with Azure Active Directory

1. Navigate to Azure Active Directory in the Azure portal.
2. If you are using a corporate Microsoft account, you might be restricted from access, in which case you would need to use a personal account for this stage of the exercise.
3. You should already have a default tenant to use, but if not, create a new tenant and fill in the required information.
4. Navigate to the "App registrations" page, and enter a name for the app, while allowing the widest set of accounts to access it.
5. Remember, you'll likely want to be more restrictive when creating your own apps.
6. After you click "Register", copy down the "Application (client) ID", as you'll need that for the next exercise.
7. Additionally, under "Manage", click "Certificates &amp; secrets", then "+ New client secret", then enter a description (you can decide on your own desired expiration time). Copy down string under "Value", and make sure you store it somewhere safe.

## Add Add the redirect and logout URIs in Azure AD

1. Within your registered app, under "Manage", click on "Authentication", then "+Add a platform".
2. Select "Web" under "Web applications" in the new window.
3. Enter https://localhost:5555/getAToken in the redirect URI (replace /getAToken with your own REDIRECT_PATH).
4. Enter https://localhost:5555/login in the logout URI - we want the user to be redirected back to the login page of this app when they logout.
 Other apps could potentially just redirect back to a homepage (our homepage is hidden behind the login process).

## App configuration and deployment
**Note**: This app will be served on `https` only as Azure AD will block insecure connections for redirect URIs on deployed applications. As such, when testing on `localhost`, make sure to add `https` at the start instead of `http`, e.g. `https://localhost:5555`.

1. You can launch the app, if desired, to start, but you'll notice that it doesn't yet allow you to log in with your Microsoft account. To start, open up `config.py`, and enter in both the client secret and application client ID you previously copied down from Azure AD. If your app is no longer registered, go back through the steps in the previous exercise to obtain new values.
2. You'll also notice a variable for `REDIRECT_PATH`. This should start with a `/`, and then can be whatever else you want it to be (although you should stay away from `/home`, `/login` or `/logout`, since those are used elsewhere in the app). Once you have this set, go back to Azure AD and enter this as the redirect URI for your app, as well as adding a logout URI.
3. Now, you're ready to get started with `msal`. The app code contained in `views.py` currently implements a bit of basic log in and logout with the `Flask-Login` library, but you need to implement the TODOs throughout for the "Sign in with Microsoft" button on the app to work appropriately. The suggested order is as follow:
    - Implement `_build_msal_app` to create a `ConfidentialClientApplication` object.
        - This class requires a Client ID and Client Secret from Azure AD.
        - It also requires an “authority” based on single or multi-tenant access.
        For example, https://login.microsoftonline.com/common is for multi-tenant access whereas single tenant
         access would replace /common with a tenant id
        - We can also pass in an optional argument for a cached session to avoid re-requesting information.
    - Implement `_build_auth_url` to get an authorization request URL using the the `get_authorization_request_url` function.
    This requires:
        - A scope, such as USER.READ
        - State (UUID in our case, identifying the session)
        - Redirect URI
    - Acquire a token from an msal app within the `authorized` function using the `acquire_token_by_authorization_code` method
    - Add the appropriate logout URL to the `logout` function
    
    Together, the above four steps should allow you to have a functional "Sign in with Microsoft" button with the Microsoft Authentication Library, as well as to log back out of the related Microsoft account.
4. Test your app out in localhost (making sure to use `https`), or feel free to deploy the app as well.

Note: A Tenant is ypically equivalent to an organization in Azure AD, although you can set up additional tenants as necessary.
