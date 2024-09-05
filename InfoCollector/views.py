from django.shortcuts import render

# Create your views here.
def InfoCollect(request):
    ip = get_client_ip(request)
    browser = get_browser(request)
    os = get_os(request)
    # print(request.__dict__)
    print(request.META.get('HTTP_USER_AGENT', ''))
    # user_agent = request.META.get('HTTP_USER_AGENT', '')
    # ua = parse(user_agent)
    # browser = ua.browser.family
    # os = ua.os.family
    context = {
        'ip': ip,
        'browser': browser,
        'os': os,
    }
    return render(request, 'InfoCollector.html', context)

##################################
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_browser(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')

    # Determine the browser
    if 'MSIE' in user_agent or 'Trident/' in user_agent:
        browser = 'Internet Explorer'
    elif 'Firefox' in user_agent:
        browser = 'Firefox'
    elif 'Chrome' in user_agent and 'Safari' in user_agent:
        browser = 'Chrome'
    elif 'Safari' in user_agent and not 'Chrome' in user_agent:
        browser = 'Safari'
    elif 'Opera' in user_agent or 'OPR/' in user_agent:
        browser = 'Opera'
    elif 'Edge' in user_agent:
        browser = 'Edge'
    else:
        browser = 'Unknown'

    return browser

################################################

def get_os(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')

    # Determine the operating system
    if 'Windows' in user_agent:
        os = 'Windows'
    elif 'Macintosh' in user_agent or 'Mac OS X' in user_agent:
        os = 'Mac OS'
    elif 'Linux' in user_agent:
        os = 'Linux'
    elif 'Android' in user_agent:
        os = 'Android'
    elif 'iPhone' in user_agent or 'iPad' in user_agent:
        os = 'iOS'
    else:
        os = 'Unknown'

    return os

