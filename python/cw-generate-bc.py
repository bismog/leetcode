#!/usr/bin/env python

# ("mysite.com/pictures/holidays.html", " : ")  
#                                               -->   '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
# ("www.codewars.com/users/GiacomoSorbi?ref=CodeWars", " / ")
#                                               -->   '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
# ("www.microsoft.com/docs/index.htm#top", " * ")
#                                               -->   '<a href="/">HOME</a> * <span class="active">DOCS</span>'
# ("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp", " > ")
#                                               -->   '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'
# ("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + ")
#                                               -->   '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'


sources = \
[
    {
        "url": "mysite.com/pictures/holidays.html",
        "seperator": ":"
    },
    {
        "url": "www.codewars.com/users/GiacomoSorbi?ref=CodeWars",
        "seperator": "/"
    },
    {
        "url": "www.microsoft.com/docs/index.htm#top",
        "seperator": "*"
    },
    {
        "url": "mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp",
        "seperator": ">"
    },
    {
        "url": "www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi",
        "seperator": "+"
    }
]
 

def find_span(url):
    left,sep,right = url.rpartition('/')
    right_no_suffix = right.split('.')[0]
    # if not cmp('index', right_no_suffix):
    if cmp('index', right_no_suffix):
        span = right.split('?')[0].split('#')[0].split('.')[0].upper().replace('-', ' ')
        url_o = left
    else:
        url_o, span = find_span(left)
    return (url_o, span)

def contract(ss):
    ignores = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
    if len(ss) > 30:
        ss_out = ''.join([ s[0] for s in ss.split('-') if not s in ignores ])
    else:
        ss_out = ss
    # print ss_out
    return ss_out

def generate_bc(url, seperator):
    """
    """
    # Find span class
    url_just, span = find_span(url)
    # print url_just, "\t", span

    # Handle each href
    hrefs = url_just.split('/')[1:]

    ## Replace the first href
    out = '<a href="/">HOME</a>' + '' + seperator + ''
    if hrefs:
        href_outs = [ (href, contract(href).upper()) for href in hrefs ]
        # print href_outs
        
        for ho in href_outs:
            out = out + '<a href="/' + ho[0] + '/">' + ho[1] + '</a>' + seperator + ''

    out = out + '<span class="active">' + span + '</span>'
    return out


if __name__ == "__main__":
    for source in sources:
        out = generate_bc(source["url"], source["seperator"])
        print out
