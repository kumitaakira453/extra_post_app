from django.views.defaults import (
    bad_request,
    page_not_found,
    permission_denied,
    server_error,
)

ERROR_400_TEMPLATE_NAME = "errors/400.html"
ERROR_403_TEMPLATE_NAME = "errors/403.html"
ERROR_404_TEMPLATE_NAME = "errors/404.html"
ERROR_500_TEMPLATE_NAME = "errors/500.html"


# 400
def custom_bad_request(request, exception, template_name=ERROR_400_TEMPLATE_NAME):
    return bad_request(request, exception, template_name=template_name)


# 403
def custom_permission_denied(request, exception, template_name=ERROR_403_TEMPLATE_NAME):
    return permission_denied(request, exception, template_name=template_name)


# 404
def custom_page_not_found(request, exception, template_name=ERROR_404_TEMPLATE_NAME):
    return page_not_found(request, exception, template_name=template_name)


# 500
def custom_server_error(request, template_name=ERROR_500_TEMPLATE_NAME):
    return server_error(request, template_name=template_name)
