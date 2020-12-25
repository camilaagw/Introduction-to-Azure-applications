class Config(object):
    # In a production app, store this instead in KeyVault or an environment variable
    CLIENT_SECRET = "GPQ_~iS-jFdvN4ewbax41ogJgr~Y0648ZA"

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "0febddbd-1f46-4a3a-99bb-5f1e5adba7b6"

    # TODO: Enter the redirect path you want to use for OAuth requests
    #   Note that this will be the end of the URI entered back in Azure AD
    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL,
        # which must match your app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session